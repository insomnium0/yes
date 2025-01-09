from lupa import LuaRuntime

# Initialize Lua runtime
lua = LuaRuntime()

# Load and execute the Lua script
with open('Lua/lua_script.lua', 'r') as lua_file:
    lua_code = lua_file.read()

lua.execute(lua_code)