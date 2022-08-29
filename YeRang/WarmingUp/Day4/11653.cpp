#include <iostream>
using namespace std;

void demical(int n) {
    if (n == 1) {
        return;
    }
    else {
        int d = -1;
        for(int i = 2; i <= n; i++){
            if (n % i == 0) {
                printf("%d\n", i);
                demical(n/i);
                return;
            }
        }
        printf("%d\n", n);
        return;
    }
}

int main() {
    int num;
    scanf("%d", &num);
    demical(num);
    return 0;
}