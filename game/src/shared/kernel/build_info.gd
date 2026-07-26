class_name BuildInfoFacade
extends Node

const BUILD_ID_SETTING: StringName = &"outsurvive/build/build_id"
const EXPECTED_ENGINE_VERSION_SETTING: StringName = &"outsurvive/build/expected_engine_version"
const VALID_BUILD_ID_CHARACTERS: String = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
const REQUIRED_ENGINE_FIELDS: Array[String] = ["major", "minor", "patch", "status", "build"]

static func build_id() -> String:
	var configured_build_id: Variant = ProjectSettings.get_setting(BUILD_ID_SETTING, "")
	if typeof(configured_build_id) != TYPE_STRING:
		return ""
	return configured_build_id


static func expected_engine_version() -> Dictionary:
	var configured_version: Variant = ProjectSettings.get_setting(EXPECTED_ENGINE_VERSION_SETTING, {})
	if typeof(configured_version) != TYPE_DICTIONARY:
		return {}
	return configured_version.duplicate(true)


static func engine_version() -> Dictionary:
	return Engine.get_version_info().duplicate(true)


static func diagnostic_fields() -> Dictionary:
	return {
		"build_id": build_id(),
		"engine_version": engine_version(),
	}


static func validate_runtime() -> OperationResult:
	return validate_values(build_id(), expected_engine_version(), engine_version())


static func validate_values(
	build_id_value: Variant,
	expected_engine_value: Variant,
	actual_engine_value: Dictionary,
) -> OperationResult:
	if typeof(build_id_value) != TYPE_STRING:
		return OperationResult.failure(
			&"BOOT_BUILD_ID_INVALID",
			{"actual_type": type_string(typeof(build_id_value))},
		)

	if build_id_value.is_empty():
		return OperationResult.failure(&"BOOT_BUILD_ID_MISSING")

	for index: int in range(build_id_value.length()):
		var character: String = build_id_value.substr(index, 1)
		if VALID_BUILD_ID_CHARACTERS.find(character) == -1:
			return OperationResult.failure(
				&"BOOT_BUILD_ID_INVALID",
				{"build_id": build_id_value},
			)

	if typeof(expected_engine_value) != TYPE_DICTIONARY:
		return OperationResult.failure(&"BOOT_ENGINE_CONFIGURATION_INVALID")

	for field_name: String in REQUIRED_ENGINE_FIELDS:
		if not expected_engine_value.has(field_name):
			return OperationResult.failure(
				&"BOOT_ENGINE_CONFIGURATION_INVALID",
				{"missing_field": field_name},
			)
		if actual_engine_value.get(field_name) != expected_engine_value.get(field_name):
			return OperationResult.failure(
				&"BOOT_ENGINE_VERSION_MISMATCH",
				{
					"field": field_name,
					"expected": expected_engine_value.get(field_name),
					"actual": actual_engine_value.get(field_name),
				},
			)

	return OperationResult.success(
		{
			"build_id": build_id_value,
			"engine_version": actual_engine_value.duplicate(true),
		},
	)
