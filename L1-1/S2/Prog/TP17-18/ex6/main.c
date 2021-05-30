#include <stdio.h>

const int JEU_DE_BASE[7] = {1, 1, 1, 0, 2, 2, 2};
const int JEU_FINI[7] = {2, 2, 2, 0, 1, 1, 1};

int verifieEgal(int *tab1, int *tab2) {
    for (int i = 0; i < 7; i++) {
        if (tab1[i] != tab2[i]) {
            return 0;
        }
    }
    return 1;
}

void affiche(int *jeu) {
    for (int i = 0; i < 7; i++) {
        if (jeu[i] == 1) {
            printf("|g|");
        } else if (jeu[i] == 2) {
            printf("|d|");
        } else if (jeu[i] == 0) {
            printf("| |");
        } else {
            printf("Erreur case numero %d\nsortie du programme", i);
            break;
        }
    }
    printf("\n");
    for (int i = 0; i < 7; i++) {
        printf("|%d|", i);
    }
    printf("\n");
}

void echange(int i, int j, int *tab) {
    int temp = tab[i];
    tab[i] = tab[j];
    tab[j] = temp;
}

int coupJouable(int *tab, int i) {
    if ((i < 6) && (tab[i+1] == 0)) {
        return 11;
    } else if ((i < 5) && (tab[i+2] == 0)) {
        return 12;
    } else if ((tab[i] == 2) && (tab[i-1] == 0)) {
        return 21;
    } else if ((tab[i] == 2) && (tab[i-2] == 0)) {
        return 22;
    } else {
        return 0;
    }
}

int jouerCoup(int *tab) {
    int coupVoulu;
    affiche(tab);
    printf("Quelle grenouille voulez-vous deplacer?\nTapez le numero de sa case\nTapez 111 pour arreter la partie\nTapez 222 pour recommencer");
    scanf("%d", &coupVoulu);
    if (coupVoulu == 111) {
        return 111;
    } else if (coupVoulu == 222) {
        return 222;
    } else if (coupJouable(tab, coupVoulu) == 11) {
        echange(coupVoulu, coupVoulu+1, tab);
        return 11;
    } else if (coupJouable(tab, coupVoulu) == 12) {
        echange(coupVoulu, coupVoulu + 2, tab);
        return 12;
    } else if (coupJouable(tab, coupVoulu) == 21) {
        echange(coupVoulu, coupVoulu - 1, tab);
        return 21;
    } else if (coupJouable(tab, coupVoulu) == 22) {
        echange(coupVoulu, coupVoulu - 2, tab);
        return 22;
    } else {
        printf("Erreur\n");
    }
}

void partie() {
    int jeu[7] = {2, 2, 0, 2, 1, 1, 1};
    int coup = -1;
    while (1) {
        coup = jouerCoup(jeu);
        if ((verifieEgal(jeu, JEU_FINI) == 1) || (coup == 111)) {
            break;
        }
        if (coup == 222) {
            for (int i = 0; i < 7; i++) {
                jeu[i] = JEU_DE_BASE[i];
            }
        }
    }
    if (verifieEgal(jeu, JEU_FINI) == 1) {
        printf("Vous avez reussi!");
    }
}

int main() {
    int choix;
    do {
        partie();
        printf("Voulez-vous rejouer?\n1 ou 0");
        scanf("%d", &choix);
    } while(choix == 1);

    return 0;
}
