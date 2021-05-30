#include <stdio.h>

void affiche(int n) {
    for (int i = 0; i < n; i++) {
        printf("* ");
    }
    printf("\n");
}

int min(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int saisie(int a, int b) {
    int choix = -1;
    while (choix > b || choix < a) {
        printf("Veuillez entrer un nombre entre %d et %d", a, b);
        scanf("%d", &choix);
    }
    return choix;
}

int main() {
    const int NB_MINI = 1;
    const int NB_MAXI = 3;

    int nbAllumettes = 20;
    int joueur = 1;
    int aRetirer;

    while (1) {
        affiche(nbAllumettes);
        printf("\nJoueur %d, combien d'allumettes voulez-vous retirer? Il en reste %d\n", joueur, nbAllumettes);
        aRetirer = saisie(NB_MINI, NB_MAXI);
        nbAllumettes -= aRetirer;

        if (nbAllumettes < 1) {
            printf("Le joueur %d a perdu", joueur);
            break;
        }

        if (joueur == 1) {
            joueur = 2;
        } else {
            joueur = 1;
        }
    }
    return 0;
}
