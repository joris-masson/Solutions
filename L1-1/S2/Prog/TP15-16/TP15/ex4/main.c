#include <stdio.h>
#include <math.h>

float leA(int x) {
    return sqrt(1 + x);
}

float suite(int n) {
    float res = 3;
    for(int i = 0; i <= n; i++) {
        res = sqrt(1 + res);
    }
    return res;
}

int main() {
    printf("%f", suite(3));
    return 0;
}
