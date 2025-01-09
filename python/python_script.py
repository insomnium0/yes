import ctypes

mylib = ctypes.CDLL('../yes/c/mylibrary.so')
mylib.c_hello()
