#include <stdio.h>

int main() {
    const int PIERRE = 1, FEUILLE = 2, CISEAUX = 3;

    int choixJ1, choixJ2;

    printf("Pierre:%d\nFeuille:%d\nCiseaux:%d", PIERRE, FEUILLE, CISEAUX);
    printf("\nChoix Joueur 1: ");
    scanf("%d",&choixJ1);
    if ((choixJ1 != PIERRE) && (choixJ1 != FEUILLE) && (choixJ1 != CISEAUX)) {
        printf("\nLe joueur 1 a mal saisi.");
    } else {
        printf("\nPierre:%d\nFeuille:%d\nCiseaux:%d", PIERRE, FEUILLE, CISEAUX);
        printf("\nChoix Joueur 2: ");
        scanf("%d",&choixJ2);
        if ((choixJ1 != PIERRE) && (choixJ1 != FEUILLE) && (choixJ1 != CISEAUX)) {
            printf("\nLe joueur 2 a mal saisi.");
        } else {
            if ((choixJ1 == 1 && choixJ2 == 3) || (choixJ1 == 2 && choixJ2 == 1) || (choixJ1 == 3 && choixJ2 == 2)) {
                printf("\nLe joueur 1 gagne.");
            } else {
                printf("\nLe joueur 2 gagne.");
            }
        }
    }
    return 0;
}
