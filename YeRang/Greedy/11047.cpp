//
// Created by 박예랑 on 2023/01/01.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k, cnt = 0;
    int nV[10];

    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &nV[i]);
    }

    for (int i = n-1; i >= 0; i--) {
        if (nV[i] <= k) {
            cnt += k/nV[i];
            k = k % nV[i];
        }
        if (k <= 0) break;
    }
    printf("%d\n", cnt);

    return 0;
}