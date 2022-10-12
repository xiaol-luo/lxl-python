pyinstaller.exe -F script_root/main_entrance.py  ^
--collect-submodules script_root/examples/gen_lua_config ^
-p script_root ^
--hidden-import examples.gen_lua_config.main ^
--add-data  "script_root/examples/gen_lua_config/impl/tt/templates;examples/gen_lua_config/impl/tt/templates"