#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n=0, m=0;
char map[101][101] = {0,};
bool visited[101][101] = {0, };
int w = 0, b = 0;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int recursive(int x, int y, char c) {
    int sum = 1;
    visited[x][y] = 1;

    for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if ((nx < m && nx >=0) && (ny < n && ny >=0) && !visited[nx][ny] && c == map[nx][ny]) {
            sum += recursive(nx, ny, c);
        }
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin>>map[i][j];
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                char c = map[i][j];
                int res = recursive(i,j, c);
                (c == 'W') ? w += res*res : b += res*res;
            }
        }
    }
    cout << w << ' ' << b;

    return 0;
}
