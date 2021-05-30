#include <stdio.h>

float moyenne(int x, int y) {
    float moy = 0;
    moy = (x+y)/2.0;

    return moy;
}

int main() {
    printf("%f\n", moyenne(15, 17));
    printf("%f\n", moyenne(15, 16));
    return 0;
}
