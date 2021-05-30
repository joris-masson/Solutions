#include <stdio.h>
#include <math.h>

int afficheTab(int *tab, int taille) {
    int cp = 0;
    for (int i = 0; i < taille; i++) {
        if (tab[i] != 0) {
            printf(" - %d - ", tab[i]);
        } else {
            cp++;
        }
    }
    return cp;
}

void annuleTableau(int *tab, int taille, int val) {
    for (int i = 2*val; i < taille; i++) {
        if (tab[i]%val == 0) {
            tab[i] = 0;
        }
    }
}

int nonNul(int *tab, int taille, int val) {
    for (int i = 0; i < taille; i++) {
        if (tab[i] != 0 && tab[i] >= val+1) {
            return i;
        }
    }
}

int main() {
    int tableau[1000] = {};
    int k = 2;

    for (int i = 0; i < 1000; i++) {
        tableau[i] = i;
    }
    for (int i = 0; i < sqrt(1000); i++) {
        annuleTableau(tableau, 1000, k);
        k = nonNul(tableau, 1000, k);
    }
    afficheTab(tableau, 1000);
    return 0;
}
