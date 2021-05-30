#include <stdio.h>

int main() {
    int n;
    float res = 1, compt = 2;
    printf("Valeur que vous voulez atteindre: ");
    scanf("%d", &n);

    while(res < n) {
        res += 1/compt;
        compt++;
    }
    printf("\nIl faut n = %f", compt-1);

    return 0;
}
