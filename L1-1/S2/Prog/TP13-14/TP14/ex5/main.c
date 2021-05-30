#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));

    int max, min = 1;
    int repJoueur, compteur = 0;
    int choixOrdi, niveau;
    int limite;

    while ((niveau != 1) && (niveau != 2) && (niveau != 3) && (niveau != 1000)) {
        printf("\nVeuillez choisir un niveau(1, 2, 3, 1000): ");
        scanf("%d", &niveau);
    }
    if (niveau == 1) {
        max = 10;
        limite = 42;
    } else if (niveau == 2) {
        max = 50;
        limite = 15;
    } else if (niveau == 3) {
        max = 100;
        limite = 10;
    } else {
        max = rand()%10000;  // Bonne chance :)
        limite = rand()%(5)+7;  // J'espère pour vous que vous êtes chanceux :D
    }

    choixOrdi = rand()%(min-max)+min;
    // printf("\n%d", choixOrdi);  // tricherie !
    while(1) {
        printf("\nVotre proposition?, il vous reste %d essai(s) ", limite-compteur);
        scanf("%d", &repJoueur);

        if (compteur >= limite-1) {
            printf("\nVous avez depasse la limite, la reponse etait %d", choixOrdi);
            break;
        }

        if (repJoueur == 0) {
            printf("\nLa reponse est: %d", choixOrdi);
            break;
        } else if (repJoueur == choixOrdi) {
            printf("\nBravo, en %d essais", compteur);
            break;
        } else if (repJoueur < choixOrdi) {
            compteur++;
            printf("\nC'est plus grand");
        } else if (repJoueur > choixOrdi) {
            compteur++;
            printf("\nC'est plus petit");
        }
    }


    return 0;
}
