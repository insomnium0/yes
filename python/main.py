import ctypes
import os
from lupa import LuaRuntime


# --- C Integration ---
# Load the shared C library
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.abspath('../c/mylibrary.so')  # Adjust as needed
mylib = ctypes.CDLL(lib_path)

# Call the C function
print("Calling C function:")
mylib.c_hello()

# --- Lua Integration ---
# Initialize Lua runtime
print("\nCalling Lua script:")
lua = LuaRuntime()

# Execute Lua code
lua_code = """
print("Hello from Lua!")
"""
lua.execute(lua_code)