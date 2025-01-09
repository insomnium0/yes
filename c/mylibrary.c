#include <stdio.h>

// Mark the function for export
#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT __attribute__((visibility("default")))
#endif

EXPORT void c_hello() {
    printf("Hello from C!\n");
}