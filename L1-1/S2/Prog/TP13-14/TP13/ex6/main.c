#include <stdio.h>

int main() {
    int n;

    printf("Que vaut n? ");
    scanf("%d", &n);

    for (int y = 0; y < n; y++) {
        printf("\n");
        for (int x = 0; x < n; x++) {
            if (y > x) {
                printf("+");
            } else {
                printf("*");
            }
        }
    }

    return 0;
}
