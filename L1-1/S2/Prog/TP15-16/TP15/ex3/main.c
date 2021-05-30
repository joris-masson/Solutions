#include <stdio.h>

int facto(int n) {
    int res = 1;
    for (int i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

int main() {
    int entier1;
    int entier2;

    printf("Entier 1:");
    scanf("%d", &entier1);

    printf("\nEntier 2:");
    scanf("%d", &entier2);

    printf("La factorielle de %d est %d, et la factorielle de %d est %d.\nLeur somme fait: %d", entier1, facto(entier1), entier2, facto(entier2), facto(entier1)+facto(entier2));

    return 0;
}
