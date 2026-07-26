class_name OperationResult
extends RefCounted

var is_success: bool
var code: StringName
var context: Dictionary


func _init(
	success_value: bool,
	code_value: StringName = &"",
	context_value: Dictionary = {},
) -> void:
	is_success = success_value
	code = code_value
	context = context_value.duplicate(true)


static func success(context_value: Dictionary = {}) -> OperationResult:
	return OperationResult.new(true, &"", context_value)


static func failure(code_value: StringName, context_value: Dictionary = {}) -> OperationResult:
	return OperationResult.new(false, code_value, context_value)
