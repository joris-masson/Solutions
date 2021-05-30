#include <stdio.h>

int main() {
    int nbValeurs;
    int note;
    int totalNotes;
    float moyenne;

    printf("Combien de notes voulez-vous rentrer?");
    scanf("%d", &nbValeurs);

    for (int i = 1; i <= nbValeurs; i++) {
        printf("Valeur %d: ", i);
        scanf("%d", &note);

        totalNotes = totalNotes + note;
    }

    moyenne = totalNotes/nbValeurs;

    printf("%f", moyenne);

    return 0;
}
