#include <stdio.h>

int main() {
    int n;
    int somme;

    printf("Que vaut N? ");
    scanf("%d", &n);

    for (int i = 0; i <= n; i++) {
        if (i%2 != 0) {  // nombres impairs seulement
            somme += i;
        }
    }

    printf("\n%d", somme);

    return 0;
}
