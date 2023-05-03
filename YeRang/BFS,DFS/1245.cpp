//
// Created by yerang on 2023-04-28.
//
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
int map[70][100] = {0,};
bool visited[70][100] = {0,};
bool isBong = true;
int res = 0;

int axisY[8]={-1, 1, 0, 0, -1, -1, 1, 1};
int axisX[8]={0, 0, -1, 1, -1, 1, -1, 1};


void bfs(int y, int x) {
    int max = map[y][x];
    queue<pair<int, int>> q;
    q.push(make_pair(y, x));

    while(!q.empty()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();
        visited[y][x] = true;
        cout << "CHECK  y : " << y << " / x : " << x << endl;
        for(int i=0;i<8;i++) {
            int my = y + axisY[i];
            int mx = x + axisX[i];

            if ((my >= 0 && my < n) && (mx >= 0 && mx < m) ) {
                // 낮은 경우
                if (map[my][mx] < map[y][x]) {
                    continue;
                }
                // 큰 값 발견!
                else if (map[my][mx] > map[y][x]) {
                    isBong = false;
                    return;
                }
                // 같은 높이 봉우리일 경우
                else if (map[my][mx] == map[y][x] && !visited[my][mx]) {
                    cout << "SAME  my : " << my << " / mx : " << mx;
                    cout << " ///  y : " << y << " / x : " << x << endl;
                    cout << "same!!!" << endl;
                    q.push(make_pair(my, mx));
                }
            }
        }
    }
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            cin >> map[i][j];
        }
    }

    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if (!visited[i][j]) {
                isBong = true;
                bfs(i, j);
                if (isBong) {
                    cout << "This is bong." << endl;
                    res++;
                }
            }
            cout << endl;
        }
    }
    cout << res << endl;

    return 0;
}