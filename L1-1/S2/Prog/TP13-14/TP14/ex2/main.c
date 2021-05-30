#include <stdio.h>

int main() {
    int nbValeurs;
    int note;
    int totalNotes = 0;
    float moyenne;

    while (1 == 1) {
        printf("\nValeur %d, -1 pour lacner le calcul: ", nbValeurs + 1);
        scanf("%d", &note);

        if (note == -1) {
            break;
        } else {
            totalNotes += note;
            nbValeurs++;
        }
    }

    moyenne = totalNotes/(nbValeurs);

    printf("%f", moyenne);

    return 0;
}
