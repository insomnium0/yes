from lupa import LuaRuntime

# Initialize Lua runtime
lua = LuaRuntime()

# Execute a Lua script
lua.execute("""
print("Hello from Lua with lupa!")
""")