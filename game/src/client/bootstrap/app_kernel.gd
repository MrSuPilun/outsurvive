class_name AppKernelService
extends Node

signal lifecycle_state_changed(previous_state: int, current_state: int)

enum LifecycleState {
	BOOTING,
	READY,
	SHUTTING_DOWN,
}

var _state: int = LifecycleState.BOOTING


func _ready() -> void:
	var bootstrap_result: OperationResult = bootstrap()
	if bootstrap_result.is_success:
		return

	GameLog.emit_event(
		&"error",
		&"app_kernel",
		&"bootstrap",
		&"application_boot_failed",
		BuildInfoFacade.build_id(),
		{"code": String(bootstrap_result.code), "context": bootstrap_result.context},
	)
	get_tree().quit(1)


func bootstrap() -> OperationResult:
	var validation_result: OperationResult = BuildInfoFacade.validate_runtime()
	if not validation_result.is_success:
		return validation_result

	var transition_result: OperationResult = _transition_to(LifecycleState.READY)
	if not transition_result.is_success:
		return transition_result

	GameLog.emit_event(
		&"info",
		&"app_kernel",
		&"bootstrap",
		&"application_booted",
		BuildInfoFacade.build_id(),
		{"lifecycle_state": lifecycle_state_name()},
	)
	return transition_result


func request_shutdown(scene_tree: SceneTree) -> OperationResult:
	var transition_result: OperationResult = _transition_to(LifecycleState.SHUTTING_DOWN)
	if not transition_result.is_success:
		return transition_result

	GameLog.emit_event(
		&"info",
		&"app_kernel",
		&"bootstrap",
		&"application_shutdown_started",
		BuildInfoFacade.build_id(),
		{"lifecycle_state": lifecycle_state_name()},
	)
	scene_tree.quit(0)
	return transition_result


func lifecycle_state() -> int:
	return _state


func lifecycle_state_name() -> String:
	return LifecycleState.keys()[_state]


static func is_transition_allowed(from_state: int, to_state: int) -> bool:
	return (
		(from_state == LifecycleState.BOOTING and to_state == LifecycleState.READY)
		or (
			from_state == LifecycleState.READY
			and to_state == LifecycleState.SHUTTING_DOWN
		)
	)


func _transition_to(next_state: int) -> OperationResult:
	if not is_transition_allowed(_state, next_state):
		return OperationResult.failure(
			&"BOOT_TRANSITION_REJECTED",
			{
				"from": LifecycleState.keys()[_state],
				"to": LifecycleState.keys()[next_state],
			},
		)

	var previous_state: int = _state
	_state = next_state
	lifecycle_state_changed.emit(previous_state, _state)
	return OperationResult.success(
		{
			"from": LifecycleState.keys()[previous_state],
			"to": LifecycleState.keys()[_state],
		},
	)
