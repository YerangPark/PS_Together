#include <iostream>
using namespace std;

int main() {
    int score, sum=0;
    for (int i=0;i<5;i++){
        scanf("%d",&score);
        sum += (score < 40) ? 40 : score;
    }
    printf("%d\n", sum/5);
    return 0;
}