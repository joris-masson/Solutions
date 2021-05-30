#include <stdio.h>

int main() {
    int age, sexe;

    printf("Quel est votre sexe?(0 pour femme, 1 pour homme) ");
    scanf("%d", &sexe);

    printf("\nQuel age avez-vous? ");
    scanf("%d", &age);

    if (((age > 20) && (sexe == 1)) || ((age >= 18) && (age <= 35) && (sexe == 0))) {
        printf("\nVous payez l'impot\n");
    } else {
        printf("\nVous ne payez pas l'impot\n");
    }

    return 0;
}
