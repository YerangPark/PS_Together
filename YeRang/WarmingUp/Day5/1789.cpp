#include <iostream>
using namespace std;

int main() {
    unsigned int s, n = 0, p = 1;
    scanf("%u", &s);
    while (s >= p) {
        s -= p++;
        n++;
    }
    printf("%u\n", n);
    return 0;
}
