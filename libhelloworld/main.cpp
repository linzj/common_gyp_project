#include <stdio.h>
extern "C" {
    void helloworld(const char* name) {
        printf("hello: %s.\n", name);
    }
}
