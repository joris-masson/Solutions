#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int alea(int n) {
    return rand()%n+1;
}

int calcul(int n) {
    int entier1 = alea(n);
    int entier2 = alea(n);

    int choixUser;
    printf("\nLa somme de %d et %d, vaut? ", entier1, entier2);
    scanf("%d", &choixUser);

    if (choixUser == entier1+entier2) {
        printf("\nBravo");
        return 1;
    } else {
        printf("\nDommage, le resultat est %d", entier1+entier2);
        return 0;
    }
}

int serieCalcul(int n, int nb) {
    int score = 0;
    for (int i = 0; i < nb; i++) {
        score += calcul(n);
    }
    return score;
}

void serieCalculJuste(int n, int nb) {
    int score = 0;
    while (score < nb) {
        printf("\n\nVous avez %d bonne reponse, vous devez en avoir %d", score, nb);
        score += calcul(n);
    }
}

int main() {
    srand(time(NULL));
    int n, nb, mode = -1;

    printf("Quel mode voulez-vous utiliser?\n0 - SerieCalcul\n1 - SerieCalculJuste");
    while (mode != 1 && mode != 0) {
        scanf("%d", &mode);
    }

    if (mode == 0) {
        printf("\nJusqu'a combien? ");
        scanf("%d", &n);

        printf("\nCombien de calculs? ");
        scanf("%d", &nb);

        printf("\nVotre score est de %d", serieCalcul(n, nb));
    } else {
        printf("\nJusqu'a combien? ");
        scanf("%d", &n);

        printf("\nCombien de calculs juste? ");
        scanf("%d", &nb);

        serieCalculJuste(n, nb);
        printf("\nVous avez termine");
    }
    return 0;
}
