#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int nbFace = 0, nbPile = 0, nbLancePile = 0, nbLanceFace = 0, lance;

    /*
     * 0 -> face
     * 1 -> pile
     */

    while (nbFace != 100) {
        nbLanceFace++;
        lance = rand()%2;;
        if (lance == 0) {
            nbFace++;
        }
    }
    while (nbPile != 100) {
        nbLancePile++;
        lance = rand()%2;;
        if (lance == 1) {
            nbPile++;
        }
    }
    printf("IL a fallu %d lancer pour atteindre 100 pile et %d lancer pour 100 face", nbLancePile, nbLanceFace);

    return 0;
}