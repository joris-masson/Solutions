#include <stdio.h>

int main() {
    float x;
    float y;

    printf("X: ");
    scanf("%f", &x);

    printf("\nY: ");
    scanf("%f", &y);

    printf("\nX = %f et Y = %f, et leur somme fait %f\n", x, y, x+y);

    return 0;
}
