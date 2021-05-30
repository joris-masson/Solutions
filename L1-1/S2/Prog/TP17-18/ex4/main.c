#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int alea(int max) {
    return rand()%max+1;
}

void affiche(int *tab, int taille) {
    for (int i = 0; i < taille; i++) {
        printf("Le nombre de %d est: %d\n", i+1, tab[i]);
    }
}

void tirage(int *tab) {
    int leTir;
    for (int i = 0; i < 100; i++) {
        leTir = alea(6);
        switch(leTir) {
            case 1:
                tab[0]++;
                break;
            case 2:
                tab[1]++;
                break;
            case 3:
                tab[2]++;
                break;
            case 4:
                tab[3]++;
                break;
            case 5:
                tab[4]++;
                break;
            case 6:
                tab[5]++;
                break;
        }
    }
}

void ajoute(int *tab, int *cumul) {
    for (int i = 0; i < 6; i++) {
        cumul[i] += tab[i];
    }
}

int main() {
    srand(time(NULL));
    int unTirage[6] = {};
    int res[6] = {};

    int demandeUtil = 1;

    do {
        tirage(unTirage);
        ajoute(unTirage, res);
        affiche(res, 6);
        printf("Voulez-vous faire un nouveau tirage? (1 ou 0)\n");
        scanf("%d", &demandeUtil);
    } while (demandeUtil == 1);
    return 0;
}
