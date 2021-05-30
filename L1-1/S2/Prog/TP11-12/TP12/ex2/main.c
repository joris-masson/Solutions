#include <stdio.h>

int main() {
    float a, b, res;
    int op;

    printf("Nombre 1: ");
    scanf("%f", &a);

    printf("\nNombre 2: ");
    scanf("%f", &b);

    printf("\nQuel operateur?\n1 - +\n2 - *\n3 - -\n4 - /");
    scanf("%d", &op);

    switch(op) {
        case 1:
            res = a + b;
            printf("%f + %f = %f", a, b, res);
            break;
        case 2:
            res = a * b;
            printf("%f * %f = %f", a, b, res);
            break;
        case 3:
            res = a - b;
            printf("%f - %f = %f", a, b, res);
            break;
        case 4:
            res = a / b;
            printf("%f / %f = %f", a, b, res);
            break;
    }

    return 0;
}
