//
// Created by 박예랑 on 2023/01/01.
//

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, sum=0;
    vector<int> v;

    scanf("%d", &n);
    for (int i=0;i<n;i++) {
        int tmp;
        scanf("%d", &tmp);
        v.push_back(tmp);
    }
    sort(v.begin(), v.end());
    for (int i=0; i<n; i++){
        sum+=v[i]*(n-i);
    }
    printf("%d\n",sum);

    return 0;
}