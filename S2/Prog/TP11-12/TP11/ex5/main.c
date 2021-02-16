#include <stdio.h>

int main() {
    int age;
    char sexe;

    printf("Quel est votre sexe?(f pour femme, h pour homme) ");
    scanf("%c", &sexe);

    printf("\nQuel age avez-vous? ");
    scanf("%d", &age);

    if (((age > 20) && (sexe == 'h')) || ((age >= 18) && (age <= 35) && (sexe == 'f'))) {
        printf("\nVous payez l'impot\n");
    } else {
        printf("\nVous ne payez pas l'impot\n");
    }

    return 0;
}
