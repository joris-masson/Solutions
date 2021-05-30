#include <stdio.h>

int compte(float *tab, int taille, int val) {
    int compteur = 0;
    for (int i = 0; i < taille; i++) {
        if (tab[i] > val) {
            compteur++;
        }
    }
    return compteur;
}

float moyenne(float *tab, int taille) {
    float somme = 0;
    for (int i = 0; i < taille; i++) {
        somme += tab[i];
    }
    return somme/(taille*1.0);
}

int min(float *tab, int taille) {
    float leMin = tab[0];
    int indice = 0;
    for (int i = 0; i < taille; i++) {
        if (tab[i] < leMin) {
            indice = i;
            leMin = tab[i];
        }
    }
    return indice;
}

int max(float *tab, int taille) {
    float leMax = tab[0];
    int indice = 0;
    for (int i = 0; i < taille; i++) {
        if (tab[i] > leMax) {
            indice = i;
            leMax = tab[i];
        }
    }
    return indice;
}

void farenheit(float *tab, int taille) {
    float tempF;
    for (int i = 0; i < taille; i++) {
        tempF = ((1.8 * tab[i]) + 32);
        tab[i] = tempF;
    }
}

void affiche(float *tab, int taille) {
    for (int i = 0; i < taille; i++) {
        printf("La valeur %d est: %f\n", i+1, tab[i]);
    }
}

void saisie(float *tab, int taille) {
    for (int i = 0; i < taille; i++) {
        printf("Valeur pour le mois %d:\n ", i+1);
        scanf("%f", &tab[i]);
    }
}

int main() {
    float tableau1[12] = {8.1, 2.3, 7.4, 14.3, 16.8, 21.1, 21.2, 20, 15.5, 14.4, 8.5, 5.8};
    printf("%d\n", compte(tableau1, 12, 20));
    printf("%f\n", moyenne(tableau1, 12));
    printf("%d, donc %f\n", min(tableau1, 12), tableau1[min(tableau1, 12)]);
    printf("%d, donc %f\n", max(tableau1, 12), tableau1[max(tableau1, 12)]);
    farenheit(tableau1, 12);
    affiche(tableau1, 12);

    saisie(tableau1, 12);
    farenheit(tableau1, 12);
    affiche(tableau1, 12);
    return 0;
}
