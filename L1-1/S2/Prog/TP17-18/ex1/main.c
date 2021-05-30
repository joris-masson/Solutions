#include <stdio.h>

int avecZero(int tab[], int longueur) {
    for (int i = 0; i < longueur; i++) {
        if (tab[i] == 0) {
            return 1;
        }
    }
    return 0;
}

int queDesZeros(int *tab, int longeur) {
    for (int i = 0; i < longeur; i++) {
        if (tab[i] != 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int unTableau[6] = {4, 5, 8, 0, 20, 480};
    int unTableau2[5] = {0, 0, 0, 0, 0};
    printf("%d\n", avecZero(unTableau, 6));
    printf("%d\n", queDesZeros(unTableau2, 5));
    return 0;
}
