# Content Source

Owner: Raw content and DCC sources.

This root contains authoring inputs, not runtime-ready game content. Production
runtime code must never load or depend on files from `content-source`; content must
pass the project bake and promotion pipeline before becoming consumable.
