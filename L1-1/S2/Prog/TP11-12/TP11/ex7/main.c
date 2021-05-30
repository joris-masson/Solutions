#include <stdio.h>

int main() {
    int note1;
    int note2;
    int note3;
    int note4;
    int sommeNotes;
    int mentionVoulue;
    float moyenne;
    float notePourPasser;

    printf("Les notes doivent être comprises entre 0 et 20.");
    printf("\nNote1: ");
    scanf("%d", &note1);

    printf("\nNote2: ");
    scanf("%d", &note2);

    printf("\nNote3: ");
    scanf("%d", &note3);

    sommeNotes = (note1+note2+note3);
    moyenne = (sommeNotes/4);

    if (sommeNotes >= 40) {
        printf("\nBravo, la somme de vos notes vaut %d, ce qui est supérieur à 40, impossible de ne pas valider votre annee avec ça!", sommeNotes);

        printf("Quelle mention voulez-vous avoir?\n1 - TB\n2 - B\n3 - AB\n");
        scanf("%d", &mentionVoulue);

        if (mentionVoulue == 1) {
            notePourPasser = 48 - sommeNotes;
            printf("Il vous faudra %f", notePourPasser);
        } else if (mentionVoulue == 2) {
            notePourPasser = 42 - sommeNotes;
            printf("Il vous faudra %f", notePourPasser);
        } else if (mentionVoulue == 3) {
            notePourPasser = 36 - sommeNotes;
            printf("Il vous faudra %f", notePourPasser);
        }
    } else if (sommeNotes < 20) {
        notePourPasser =  - sommeNotes;
        printf("\nDommage, impossible de valider avec %d :(\nMais vous pouvez valider avec %f", sommeNotes, notePourPasser);
    }

    printf("\nLa moyenne des quatre notes est de %f", moyenne);

    return 0;
}
