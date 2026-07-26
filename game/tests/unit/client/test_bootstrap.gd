extends SceneTree

const OperationResultScript: Script = preload("res://src/shared/kernel/operation_result.gd")
const BuildInfoScript: Script = preload("res://src/shared/kernel/build_info.gd")
const GameLogScript: Script = preload("res://src/shared/diagnostics/game_log.gd")
const AppKernelScript: Script = preload("res://src/client/bootstrap/app_kernel.gd")

var _failure_messages: Array[String] = []
var _assertion_count: int = 0


func _init() -> void:
	call_deferred("_run")


func _run() -> void:
	_test_operation_result()
	_test_project_runtime_contract()
	_test_build_info_validation()
	_test_lifecycle_graph()
	_test_structured_log_record()
	_test_boot_root_scene()

	if _failure_messages.is_empty():
		GameLogScript.emit_event(
			&"info",
			&"bootstrap_test",
			&"unit",
			&"bootstrap_tests_passed",
			"local-dev",
			{"assertion_count": _assertion_count},
		)
		quit(0)
		return

	for failure_message: String in _failure_messages:
		push_error(failure_message)
	GameLogScript.emit_event(
		&"error",
		&"bootstrap_test",
		&"unit",
		&"bootstrap_tests_failed",
		"local-dev",
		{"failures": _failure_messages.duplicate()},
	)
	quit(1)


func _test_operation_result() -> void:
	var success: RefCounted = OperationResultScript.success({"value": 7})
	_assert_true(success.is_success, "OperationResult.success must report success")
	_assert_equal(success.code, &"", "OperationResult.success must have an empty error code")
	_assert_equal(success.context.get("value"), 7, "OperationResult.success must preserve context")

	var failure: RefCounted = OperationResultScript.failure(&"BOOT_EXPECTED_REJECTION", {"reason": "fixture"})
	_assert_false(failure.is_success, "OperationResult.failure must report failure")
	_assert_equal(failure.code, &"BOOT_EXPECTED_REJECTION", "OperationResult.failure must preserve its typed code")
	_assert_equal(failure.context.get("reason"), "fixture", "OperationResult.failure must preserve context")


func _test_project_runtime_contract() -> void:
	_assert_equal(
		ProjectSettings.get_setting("application/run/main_scene"),
		"res://scenes/boot/boot_root.tscn",
		"Project main scene must be BootRoot",
	)
	_assert_equal(
		ProjectSettings.get_setting("rendering/renderer/rendering_method"),
		"forward_plus",
		"Desktop runtime renderer must be Forward+",
	)
	_assert_equal(
		ProjectSettings.get_setting("rendering/renderer/rendering_method.mobile"),
		"mobile",
		"Mobile runtime renderer override must be Mobile",
	)
	_assert_true(ProjectSettings.has_setting("autoload/BuildInfo"), "BuildInfo autoload must exist")
	_assert_true(ProjectSettings.has_setting("autoload/AppKernel"), "AppKernel autoload must exist")
	_assert_false(ProjectSettings.has_setting("autoload/GameLog"), "GameLog must not be an autoload")
	_assert_false(
		ProjectSettings.has_setting("autoload/PlatformGateway"),
		"PlatformGateway must not exist before a consumer",
	)
	_assert_false(OS.has_feature("mono"), "Runtime must not expose the Mono feature")
	_assert_false(ClassDB.class_exists("CSharpScript"), "Runtime must not include C# scripting")


func _test_build_info_validation() -> void:
	var actual_engine: Dictionary = Engine.get_version_info()
	var expected_engine: Dictionary = {
		"major": 4,
		"minor": 7,
		"patch": 1,
		"status": "stable",
		"build": "official",
	}
	var valid_result: RefCounted = BuildInfoScript.validate_values("local-dev", expected_engine, actual_engine)
	_assert_true(valid_result.is_success, "Valid build metadata must pass")

	var missing_result: RefCounted = BuildInfoScript.validate_values("", expected_engine, actual_engine)
	_assert_false(missing_result.is_success, "Missing build ID must be rejected")
	_assert_equal(missing_result.code, &"BOOT_BUILD_ID_MISSING", "Missing build ID must use typed failure")

	var malformed_result: RefCounted = BuildInfoScript.validate_values("bad build id", expected_engine, actual_engine)
	_assert_false(malformed_result.is_success, "Malformed build ID must be rejected")
	_assert_equal(malformed_result.code, &"BOOT_BUILD_ID_INVALID", "Malformed build ID must use typed failure")

	var wrong_type_result: RefCounted = BuildInfoScript.validate_values(47, expected_engine, actual_engine)
	_assert_false(wrong_type_result.is_success, "Non-string build ID must be rejected")
	_assert_equal(
		wrong_type_result.code,
		&"BOOT_BUILD_ID_INVALID",
		"Non-string build ID must be classified as malformed",
	)

	var incomplete_engine_result: RefCounted = BuildInfoScript.validate_values(
		"local-dev",
		{"major": 4},
		actual_engine,
	)
	_assert_false(incomplete_engine_result.is_success, "Incomplete engine metadata must be rejected")
	_assert_equal(
		incomplete_engine_result.code,
		&"BOOT_ENGINE_CONFIGURATION_INVALID",
		"Incomplete engine metadata must use typed configuration failure",
	)

	var mismatched_engine: Dictionary = expected_engine.duplicate(true)
	mismatched_engine["patch"] = 0
	var mismatch_result: RefCounted = BuildInfoScript.validate_values(
		"local-dev",
		mismatched_engine,
		actual_engine,
	)
	_assert_false(mismatch_result.is_success, "Engine mismatch must be rejected")
	_assert_equal(mismatch_result.code, &"BOOT_ENGINE_VERSION_MISMATCH", "Engine mismatch must use typed failure")

	var fields: Dictionary = BuildInfoScript.diagnostic_fields()
	_assert_equal(fields.get("build_id"), "local-dev", "BuildInfo must expose build_id")
	_assert_true(fields.get("engine_version") is Dictionary, "BuildInfo must expose structured engine version")


func _test_lifecycle_graph() -> void:
	var kernel: Node = AppKernelScript.new()
	_assert_equal(kernel.lifecycle_state(), AppKernelScript.LifecycleState.BOOTING, "Kernel must start BOOTING")
	for from_state: int in AppKernelScript.LifecycleState.values():
		for to_state: int in AppKernelScript.LifecycleState.values():
			var expected_allowed: bool = (
				(
					from_state == AppKernelScript.LifecycleState.BOOTING
					and to_state == AppKernelScript.LifecycleState.READY
				)
				or (
					from_state == AppKernelScript.LifecycleState.READY
					and to_state == AppKernelScript.LifecycleState.SHUTTING_DOWN
				)
			)
			_assert_equal(
				AppKernelScript.is_transition_allowed(from_state, to_state),
				expected_allowed,
				"Lifecycle edge %s -> %s must match exact graph"
				% [
					AppKernelScript.LifecycleState.keys()[from_state],
					AppKernelScript.LifecycleState.keys()[to_state],
				],
			)

	var start_result: RefCounted = kernel.bootstrap()
	_assert_true(start_result.is_success, "Kernel bootstrap must transition to READY")
	_assert_equal(kernel.lifecycle_state(), AppKernelScript.LifecycleState.READY, "Kernel must reach READY")
	var duplicate_result: RefCounted = kernel.bootstrap()
	_assert_false(duplicate_result.is_success, "Duplicate bootstrap must be rejected")
	_assert_equal(
		duplicate_result.code,
		&"BOOT_TRANSITION_REJECTED",
		"Invalid lifecycle transition must use typed failure",
	)
	kernel.free()


func _test_structured_log_record() -> void:
	var record: Dictionary = GameLogScript.build_record(
		&"info",
		&"bootstrap_test",
		&"unit",
		&"record_created",
		"local-dev",
		{"fixture": true},
	)
	for required_key: String in [
		"timestamp_utc",
		"level",
		"service",
		"subsystem",
		"event",
		"build_id",
		"fields",
	]:
		_assert_true(record.has(required_key), "Structured log record must include %s" % required_key)


func _test_boot_root_scene() -> void:
	var scene_path: String = "res://scenes/boot/boot_root.tscn"
	_assert_true(ResourceLoader.exists(scene_path), "Configured BootRoot scene must exist")
	if not ResourceLoader.exists(scene_path):
		return

	var packed_scene: PackedScene = load(scene_path) as PackedScene
	_assert_true(packed_scene != null, "BootRoot resource must load as PackedScene")
	if packed_scene == null:
		return

	var boot_root: Control = packed_scene.instantiate() as Control
	_assert_true(boot_root != null, "BootRoot must instantiate as Control")
	if boot_root == null:
		return

	get_root().add_child(boot_root)
	var diagnostic_fields: Dictionary = boot_root.diagnostic_fields()
	_assert_equal(diagnostic_fields.get("build_id"), "local-dev", "BootRoot must expose build_id")
	_assert_true(
		diagnostic_fields.get("engine_version") is Dictionary,
		"BootRoot must expose structured engine version",
	)
	_assert_equal(diagnostic_fields.get("lifecycle_state"), "READY", "BootRoot must expose READY state")
	_assert_false(auto_accept_quit, "BootRoot must disable SceneTree auto-accept quit")

	var diagnostic_label: Label = boot_root.find_child("DiagnosticLabel", true, false) as Label
	_assert_true(diagnostic_label != null, "BootRoot must contain a diagnostic Label")
	if diagnostic_label != null:
		_assert_true(
			diagnostic_label.text.contains("Developer diagnostics"),
			"BootRoot must mark its text as developer diagnostics",
		)
		_assert_true(diagnostic_label.text.contains("build_id=local-dev"), "Label must show build_id")
	_assert_true(diagnostic_label.text.contains("lifecycle_state=READY"), "Label must show lifecycle")

	GameLogScript.emit_event(
		&"info",
		&"bootstrap_test",
		&"diagnostics",
		&"bootstrap_diagnostics_observed",
		String(diagnostic_fields["build_id"]),
		diagnostic_fields,
	)
	boot_root.free()


func _assert_true(value: bool, message: String) -> void:
	_assertion_count += 1
	if not value:
		_failure_messages.append(message)


func _assert_false(value: bool, message: String) -> void:
	_assert_true(not value, message)


func _assert_equal(actual: Variant, expected: Variant, message: String) -> void:
	if actual != expected:
		_failure_messages.append("%s (expected=%s actual=%s)" % [message, expected, actual])
