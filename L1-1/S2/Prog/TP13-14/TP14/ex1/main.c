#include <stdio.h>

int main() {
    const int A_ECRIRE = 33;

    int nbEssais;
    int text;

    printf("Veuillez ecrire %d ", A_ECRIRE);
    scanf("%d", &text);

    if (text == A_ECRIRE) {
        printf("Merci");
    } else {
        while (text != A_ECRIRE) {
            printf("\nNon, vous avez ecrit %d, il fallait marquer %d, veuillez reessayer: ", text, A_ECRIRE);
            scanf("%d", &text);
            nbEssais++;
        }
        printf("\nMerci, mais vous avez quand meme mis %d essais pour ecrire %d", nbEssais, A_ECRIRE);
    }

    return 0;
}
