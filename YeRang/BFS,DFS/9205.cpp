//
// Created by smsms on 2023-05-04.
//
#include <iostream>
#include <queue>
#include <tuple>
#include <stdlib.h>
using namespace std;

int t, n;
#define MAX_BEER 20
#define BEER_DIST 50


int distAtoB(int ax, int ay, int bx, int by) {
    return abs(bx-ax) + abs(by-ay);
}

int main() {
    cin >> t;
    for (int i=0; i<t; i++) {
        int conv[101][2]={0,};
        bool visitedConv[101] = {0,};
        int home[2], rock[2];
        bool isHappy = false;
        cin >> n; // 편의점 수
        cin >> home[0] >> home[1];
        for (int j=0; j<n; j++) {
            cin >> conv[j][0] >> conv[j][1];
        }
        cin >> rock[0] >> rock[1];

        if (!isHappy) {
            queue<tuple<int, int, int>> q;
            q.push(make_tuple(home[0], home[1], MAX_BEER * BEER_DIST));

            while(!q.empty()) {
                int x = get<0>(q.front());
                int y = get<1>(q.front());
                int leftDist = get<2>(q.front());
                q.pop();

                // 갈 수 있는 case check.
                // 종료조건 먼저 조사
                if (distAtoB(x, y, rock[0], rock[1]) <= leftDist) {
                    isHappy = true;
                    break;
                }
                else {
                    // 편의점마다 갈 수 있는지 조사
                    for (int k=0; k<n; k++) {
                        if (visitedConv[k]) continue;
                        int convX = conv[k][0];
                        int convY = conv[k][1];

                        if (distAtoB(x, y, convX, convY) <= leftDist) {
                            visitedConv[k] = true;
                            q.push(make_tuple(convX, convY, MAX_BEER * BEER_DIST));
                        }
                    }
                }
            }
        }
        if (isHappy) {cout << "happy" << endl;}
        else {cout << "sad" << endl;}
    }

}