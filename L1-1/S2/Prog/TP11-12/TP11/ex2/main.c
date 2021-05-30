//attention ce programme comporte des erreurs que vous devez corriger

#include <stdio.h>

int main(){
    printf("je suis un programme en langage C pour faire un calcul \n");

    int x;
    int y;
    int som;


    printf("Quelle est la valeur de l'entier x ? ");
    scanf("%d", &x);
    printf("Quelle est la valeur de l'entier y ? ");
    scanf("%d", &y);
    som=x+y;

    printf("la valeur de la somme est %d \n ",som);


    return 0;
}
