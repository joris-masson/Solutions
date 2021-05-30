#include <stdio.h>

int main() {
    int x;
    int y;
    int plusGrand;

    printf("X: ");
    scanf("%d", &x);

    printf("\nY: ");
    scanf("%d", &y);

    if (x<y) {
        plusGrand = y;
    } else {
        plusGrand = x;
    }

    printf("\nX = %d et Y = %d, et le plus grand des deux est: %d\n", x, y, plusGrand);
    return 0;
}
