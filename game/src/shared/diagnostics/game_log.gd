class_name GameLog
extends RefCounted


static func build_record(
	level: StringName,
	service: StringName,
	subsystem: StringName,
	event: StringName,
	build_id: String,
	fields: Dictionary = {},
) -> Dictionary:
	return {
		"timestamp_utc": Time.get_datetime_string_from_system(true) + "Z",
		"level": String(level),
		"service": String(service),
		"subsystem": String(subsystem),
		"event": String(event),
		"build_id": build_id,
		"fields": fields.duplicate(true),
	}


static func emit_event(
	level: StringName,
	service: StringName,
	subsystem: StringName,
	event: StringName,
	build_id: String,
	fields: Dictionary = {},
) -> void:
	var record: Dictionary = build_record(level, service, subsystem, event, build_id, fields)
	print(JSON.stringify(record))
