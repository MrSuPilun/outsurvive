class_name BootRoot
extends Control

@onready var _diagnostic_label: Label = %DiagnosticLabel


func _ready() -> void:
	get_tree().auto_accept_quit = false
	_diagnostic_label.text = diagnostic_text()
	if OS.get_cmdline_user_args().has("--bootstrap-smoke"):
		call_deferred("_request_shutdown", &"bootstrap_smoke")


func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_CLOSE_REQUEST and is_inside_tree():
		_request_shutdown(&"window_close")


func diagnostic_fields() -> Dictionary:
	var fields: Dictionary = BuildInfoFacade.diagnostic_fields()
	fields["lifecycle_state"] = AppKernel.lifecycle_state_name()
	return fields


func diagnostic_text() -> String:
	var fields: Dictionary = diagnostic_fields()
	return (
		"Developer diagnostics\nbuild_id=%s\nengine_version=%s\nlifecycle_state=%s"
		% [
			fields["build_id"],
			JSON.stringify(fields["engine_version"]),
			fields["lifecycle_state"],
		]
	)


func _request_shutdown(trigger: StringName) -> void:
	var fields: Dictionary = diagnostic_fields()
	fields["trigger"] = String(trigger)
	GameLog.emit_event(
		&"info",
		&"boot_root",
		&"diagnostics",
		&"bootstrap_diagnostics_observed",
		BuildInfoFacade.build_id(),
		fields,
	)

	var shutdown_result: OperationResult = AppKernel.request_shutdown(get_tree())
	if shutdown_result.is_success:
		return

	GameLog.emit_event(
		&"error",
		&"boot_root",
		&"bootstrap",
		&"application_shutdown_rejected",
		BuildInfoFacade.build_id(),
		{"code": String(shutdown_result.code), "context": shutdown_result.context},
	)
	get_tree().quit(1)
