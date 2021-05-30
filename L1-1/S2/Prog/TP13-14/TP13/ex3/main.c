#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    const int NB_LANCERS = 1000;

    int nbFace;
    int lance;

    /*
     * 0 -> face
     * 1 -> pile
     */

    srand(time(NULL));

    for (int i = 0; i < NB_LANCERS; i++) {
        lance = rand()%2;  //0 ou 1
        if (lance == 0) {
            nbFace++;
        }
    }
    printf("Il a eu %d, face et %d pile", nbFace, (1000-nbFace));

    return 0;
}
