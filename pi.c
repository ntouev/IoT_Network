#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {	
    int N = atoi(argv[1]);
    int r[N + 1];
    int i, k;
    int b, d;
    int c = 0;

    for (i = 0; i < N; i++) {
        r[i] = 2000;
    }

    for (k = N; k > 0; k -= 14) {
        d = 0;

        i = k;
        for (;;) {
            d += r[i] * 10000;
            b = 2 * i - 1;

            r[i] = d % b;
            d /= b;
            i--;
            if (i == 0) break;
            d *= i;
        }
        printf("%.4d", c + d / 10000);
        c = d % 10000;
    }

    return 0;
}
