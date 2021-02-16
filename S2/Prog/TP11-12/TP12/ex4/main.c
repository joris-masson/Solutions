#include <stdio.h>

int main() {
    int conv;
    float tempC, tempF;

    printf("1 - C -> F\n2 - F -> C");
    printf("\nQue voulez vous convertir? ");
    scanf("%d", &conv);

    switch(conv) {
        case 1:
            //Conv C -> F

            printf("\nVeuillez rentrer une temperature en degre Celsius: ");
            scanf("%f", &tempC);

            if (tempC > -273.15) {
                tempF = ((1.8 * tempC) + 32);
                printf("\nLa temperature est %f degre Celsius, ce qui fait %f degre Farenheit", tempC, tempF);
            } else {
                printf("\nValeure incorrecte");
            }
            break;
        case 2:
            //conv F -> C

            printf("\nVeuillez rentrer une temperature en degre Farenheit: ");
            scanf("%f", &tempF);

            if (tempF > -459.67) {
                tempC = ((tempF - 32)/1.8);
                printf("\nLa temperature est %f degre Farenheit, ce qui fait %f degre Celsius", tempF, tempC);
            } else {
                printf("\nValeure incorrecte");
            }
    }

    return 0;
}
