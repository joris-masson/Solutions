#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const char G[6] = {'g', 'a', 'u', 'c', 'h', 'e'};
const char D[6] = {'d', 'r', 'o', 'i', 't', 'e'};

void affiche(int *ligne, int taille) {
    for (int i = 0; i < taille; i++) {
        printf("|%d|", ligne[i]);
    }
    printf("\n");
}

int verifieGauche(char *sens, int taille) {
    for (int i = 0; i < taille; i++) {
        if (sens[i] != G[i]) {
            return 0;
        }
    }
    return 1;
}
int verifieDroite(char *sens, int taille) {
    for (int i = 0; i < taille; i++) {
        if (sens[i] != D[i]) {
            return 0;
        }
    }
    return 1;
}

int getNbZero(int *ligne, int taille) {
    int nbZero = 0;
    for (int i = 0; i < taille; i++) {
        if (ligne[i] == 0) {
            nbZero++;
        }
    }
    return nbZero;
}

int verifStableDroite(int *ligne, int taille) {
    int nbZero = getNbZero(ligne, taille);
    int nbZeroVu = 0;
    for (int i = 0; i < taille; i++) {
        if (ligne[i] != 0) {
            break;
        }
        nbZeroVu++;
    }
    if (nbZeroVu == nbZero) {
        return 1;
    } else {
        return 0;
    }
}

int verifStableGauche(int *ligne, int taille) {
    int nbZero = getNbZero(ligne, taille);
    int nbZeroVu = 0;
    for (int i = taille-1; i > 0; i--) {
        if (ligne[i] != 0) {
            break;
        }
        nbZeroVu++;
    }
    if (nbZeroVu == nbZero) {
        return 1;
    } else {
        return 0;
    }
}

void pousseDroite(int *ligne,int taille, int pos) {
    int temp;
    if (pos == taille-1 || ligne[pos+1] != 0) {
        ligne[pos] = ligne[pos];
    }else if (ligne[pos+1] == 0 && ligne[pos+1] != ligne[pos]) {
        temp = ligne[pos];
        ligne[pos] = ligne[pos+1];
        ligne[pos+1] = temp;
    } else {
        ligne[pos+1] = ligne[pos] * ligne[pos];
        ligne[pos] = 0;
    }
}

void pousseGauche(int *ligne,int taille, int pos) {
    int temp;
    if (pos == 0 || ligne[pos-1] != 0) {
        ligne[pos] = ligne[pos];
    }else if (ligne[pos-1] == 0 && ligne[pos-1] != ligne[pos]) {
        temp = ligne[pos];
        ligne[pos] = ligne[pos-1];
        ligne[pos-1] = temp;
    } else {
        ligne[pos-1] = ligne[pos] * ligne[pos];
        ligne[pos] = 0;
    }
}

void pousse(int *ligne, char *sens, int taille) {
    if (verifieDroite(sens, 6) == 1) {
        while (verifStableDroite(ligne, taille) != 1) {
            for (int i = 0; i <= taille; i++) {
                pousseDroite(ligne, taille, i);
            }
        }
    } else if (verifieGauche(sens, 6) == 1) {
        while (verifStableGauche(ligne, taille) != 1) {
            for (int i = 0; i <= taille; i++) {
                pousseGauche(ligne, taille, i);
            }
        }
    } else {
        printf("Erreur\n");
    }
}

int alea(int n) {
    return rand()%n+1;
}

void ajoute2(int *ligne, int taille) {
    int i;
    do {
        i = alea(taille-1);
    } while (ligne[i] != 0);
    ligne[alea(taille-1)] = 2;
}

void tour(int *ligne, int taille, char *sens) {
    ajoute2(ligne, taille);
    affiche(ligne, 10);

    printf("Quel sens?\ngauche ou droite");
    scanf("%s", sens);
    pousse(ligne, sens, 10);
}

int verif2048(int *ligne, int taille) {
    for (int i = 0; i < taille; i++) {
        if (ligne[i] == 2048) {
            return 1;
        }
    }
    return 0;
}

void partie(int *ligne, int taille, char *sens) {
    while (verif2048(ligne, taille) == 0) {
        tour(ligne, taille, sens);
    }
}

int main() {
    srand(time(NULL));
    int jeu[10] = {};
    char choixSens[6];
    partie(jeu, 10, choixSens);
    return 0;
}
