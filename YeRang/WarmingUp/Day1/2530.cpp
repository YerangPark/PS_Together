#include <stdio.h>

int main() {
    int a, b, c, ss;
    scanf("%d %d %d %d", &a, &b, &c, &ss);
    a += ss / 3600;
    ss %= 3600;
    b += ss / 60;
    ss %= 60;
    c += ss;

    if (c >= 60) {
        b++;
        c -= 60;
        
    }
    if (b >= 60) {
        a++;
        b -= 60;
    }
    if (a >= 24) a %= 24;

    printf("%d %d %d\n", a, b, c);
    return 0;
}