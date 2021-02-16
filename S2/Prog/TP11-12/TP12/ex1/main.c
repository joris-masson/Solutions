// ce programme ne fonctionne pas. A vous de le corriger

#include <stdio.h>

int main(){
    char n;
    int a;

    printf("quel est votre pseudo ?");
    scanf("%s",&n);
    printf("\nbonjour %s", n);

    printf("\nquelle est votre annee de naissance ?");
    scanf("%d",&a);
    printf("\nah vous avez %d ans", (2021 - a));
    printf("\nau revoir\n");
}
