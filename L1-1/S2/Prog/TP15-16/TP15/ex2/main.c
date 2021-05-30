#include <stdio.h>

int maximum(int a, int b) {
    if (a < b) {
        return b;
    } else {
        return a;
    }
}

int maximum4(int a, int b, int c, int d) {
    if (maximum(a, b) < maximum(c, d)) {
        return maximum(c, d);
    } else {
        return maximum(a, b);
    }
}

int main() {
    printf("%d\n", maximum(12, 1));
    printf("%d\n", maximum4(15, 3, 17, 15));
    return 0;
}
