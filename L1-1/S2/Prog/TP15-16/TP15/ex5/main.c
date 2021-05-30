#include <stdio.h>

int sommeDiv(int n) {
    int res = 0;
    for (int i = 1; i < n; i++) {
        if (n == i) {
            res += 0;
        } else if (n%i == 0) {
            res += i;
        }
    }
    return res;
}

int entierParfait(int n) {
    if (sommeDiv(n) == n) {
        return 1;
    } else {
        return 0;
    }
}

void afficherEntiersParfaits(int b) {
    printf("Les entiers parfaits plus petit que %d sont:", b);
    for (int i = 1; i < b; i++) {
        if (entierParfait(i)) {
            printf("%d ", i);
        }
    }
}

int main() {
    afficherEntiersParfaits(1000);
    return 0;
}
