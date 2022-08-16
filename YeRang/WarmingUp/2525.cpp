#include <stdio.h>
#include <time.h>
using namespace std;

int main() {
    int h, m, mm;
    scanf("%d %d %d", &h, &m, &mm);

    h += mm / 60;
    m += mm % 60;
    if (m >= 60){
        h++;
        m -= 60;
    }
    if (h >= 24) h -= 24;

    printf("%d %d\n", h, m);

    return 0;
}
