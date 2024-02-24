#include <iostream>
#include <queue>
using namespace std;

#define MAX 100

int n;
char map[MAX][MAX];
bool visited[MAX][MAX] = { 0 };
bool visited_rg[MAX][MAX] = { 0 };
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int bfs(int i, int j) {
    // cout << "check [" << i << "][" << j << "]\n";
    int cnt = 0;
    char color = map[i][j];
    queue<pair<int, int>> q;
    q.push(make_pair(i, j));

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        cnt++;

        for (int i=0; i<4; i++) {
            int xx = x + dx[i];
            int yy = y + dy[i];
            char cc = map[yy][xx];
            // cout << "    axis check [" << yy << "][" << xx << "]\n";

            if (xx<n && xx>=0 && yy<n && yy>=0 && !visited[yy][xx]) {
                if (color == cc) {
                    // cout << "    push [" << yy << "][" << xx << "]\n";
                    q.push(make_pair(yy, xx));
                    visited[yy][xx] = true;
                }
            }
        }
    }
    return 1;
}
int bfs_rg(int i, int j) {
    // cout << "check [" << i << "][" << j << "]\n";
    int cnt = 0;
    char color = map[i][j];
    queue<pair<int, int>> q;
    q.push(make_pair(i, j));

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        cnt++;

        for (int i=0; i<4; i++) {
            int xx = x + dx[i];
            int yy = y + dy[i];
            char cc = map[yy][xx];
            // cout << "    axis check [" << yy << "][" << xx << "]\n";

            if (xx<n && xx>=0 && yy<n && yy>=0 && !visited_rg[yy][xx]) {
                if (color == 'R' || color == 'G') {
                    if (cc == 'R' || cc == 'G') {
                        q.push(make_pair(yy, xx));
                        visited_rg[yy][xx] = true;
                    }
                }
                else if (color == cc) {
                    // cout << "    push [" << yy << "][" << xx << "]\n";
                    q.push(make_pair(yy, xx));
                    visited_rg[yy][xx] = true;
                }
            }
        }
    }
    return 1;
}

int main() {
    int cnt = 0, cnt_rg = 0;
    cin >> n;
    for(int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> map[i][j];
        }
    }

    for(int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (!visited[i][j]) {
                visited[i][j] = true;
                cnt += bfs(i, j);
            }
            if (!visited_rg[i][j]) {
                visited_rg[i][j] = true;
                cnt_rg += bfs_rg(i, j);
            }
        }
    }
    cout << cnt << " " << cnt_rg << endl;
    return 0;
}