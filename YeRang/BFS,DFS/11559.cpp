//
// Created by 박예랑 on 2023/05/05.
//
#include <iostream>
#include <queue>
#include <tuple>
#include <stdlib.h>
using namespace std;
#define ROW 12
#define COL 6
#define AXIS 4

char map[ROW][COL] = {'.',};
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

bool checkPooyo(int y, int x, char c, bool (&visited)[ROW][COL]) {
    int cnt = 0;
    queue<pair<int, int>> q;
    queue<pair<int, int>> axis;
    q.push(make_pair(y, x));
    axis.push(make_pair(y, x));

    while (!q.empty()) {
        int yy = q.front().first;
        int xx = q.front().second;
        q.pop();


        for (int i=0; i<AXIS; i++) {
            int dyy = yy + dy[i];
            int dxx = xx + dx[i];
            if (dyy < 0 || dyy >= ROW || dxx < 0 || dxx >= COL) continue;

            if (map[dyy][dxx] == c && !visited[dyy][dxx]) {
                visited[dyy][dxx] = true;
                cnt++;
                q.push(make_pair(dyy, dxx));
                axis.push(make_pair(dyy, dxx));
            }
        }

    }
    if (cnt >= 4) {
        while(!axis.empty()) {
            int yy = axis.front().first;
            int xx = axis.front().second;
            axis.pop();
            map[yy][xx] = '.';
        }
        return true;
    }
    else { return false; }
}

int main() {
    int res = 0;
    for (int i=0; i<ROW; i++) {
        for (int j=0; j<COL; j++) {
            cin >> map[i][j];
        }
    }

    bool isFin = false;
    while(!isFin) {
        bool visited[ROW][COL] = {0,};
        bool isPooyo = false;
        // 4개 이상 붙은 애들 check 후 지우기
        for (int i=ROW-1; i>=0; i--) {
            for (int j=COL-1; j>=0; j--) {
                if (map[i][j] != '.' && !visited[i][j]) {
                    bool tmpRes = checkPooyo(i, j, map[i][j], visited);
                    isPooyo |= tmpRes;
                }
            }
        }

        for (int j=0; j<COL; j++) {
            int emptySpace=ROW-1;
            for (int i = ROW-1; i>=0; i--) {
                if (map[i][j]=='.') continue;
                if (emptySpace > i) {
                    map[emptySpace][j] = map[i][j];
                    map[i][j] = '.';
                }
                emptySpace--;
            }
        }

        if (isPooyo) {
            res++;
        }
        else {
            isFin=true;
        }
    }
    cout << res << endl;

}