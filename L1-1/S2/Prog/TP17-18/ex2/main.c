#include <stdio.h>

int produitScalaire(int *tab1, int *tab2, int taille) {
    int somme = 0;
    for (int i = 0; i < taille; i++) {
        somme += (tab1[i]*tab2[i]);
    }
    return somme;
}

int main() {
    int tableau1[4] = {3, 0, -1, 2};
    int tableau2[4] = {1, 8, -2, -2};
    printf("%d", produitScalaire(tableau1, tableau2, 4));
    return 0;
}
