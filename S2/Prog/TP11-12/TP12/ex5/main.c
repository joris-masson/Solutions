#include <stdio.h>

int main() {
    int h, m, s;

    printf("Heure: ");
    scanf("%d", &h);

    printf("\nMinutes: ");
    scanf("%d", &m);

    printf("\nSecondes: ");
    scanf("%d", &s);

    s++;

    if (s >= 60) {
        s = 0;
        m++;
    }
    if (m >= 60) {
        m = 0;
        h++;
    }
    if (h >= 24) {
        h = 0;
    }

    printf("Apres 1 seconde, il sera %d:%d:%d", h, m, s);
    return 0;
}
