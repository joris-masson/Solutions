#include <stdio.h>

int main() {
    const int IMC_IDEAL = 23;

    float taille;
    float imc;
    float poidsIdeal;
    int sexe;
    int poids;
    int age;
    int nbEnfants;

    printf("Quel est votre poids(kg)? ");
    scanf("%d", &poids);

    printf("\nQuel est votre taille(m)? ");
    scanf("%f", &taille);

    imc = (poids/(taille*taille));
    printf("\nVotre IMC est de %f, ce qui veut dire que:", imc);

    if (imc < 16.5) {
        printf("\nVous etes en situation de denutrition, ou famine :'(");
    } else if (imc < 18.5) {
        printf("\nVous etes en situation de maigreur :(");
    } else if (imc < 25) {
        printf("\nVous etes en situation normale :)");
    } else if (imc < 30) {
        printf("\nVous etes en situation de surpoids :(");
    } else {
        printf("\nVous etes en situation d'obesite :'(");
    }

    poidsIdeal = ((taille*taille)*IMC_IDEAL);

    printf("\nEn supposant qu'un IMC de %d soit l'ideal, vous devriez faire %f kg pour l'atteindre",IMC_IDEAL, poidsIdeal);

    printf("\nMAIS, l'age et le nombre d'enfants peuvent impacter ce poids ideal, donc:");

    printf("\nQuel est votre age? ");
    scanf("%d", &age);

    printf("`\nQuel est votre sexe?(0 pour femme, 1 pour homme) ");
    scanf("%d", &sexe);

    if (sexe == 0) {
        printf("\nCombien d'enfants avez-vous?");
        scanf("%d", &nbEnfants);

        poidsIdeal = ((poidsIdeal+(0.4*(age-20))/(5+nbEnfants)));
    } else {
        poidsIdeal = ((poidsIdeal+(0.6*(age-20))/10));
    }

    printf("\nCompte tenu de ces informations, votre poids ideal serait de: %f kg\n", poidsIdeal);

    return 0;
}
