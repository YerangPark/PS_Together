//
// Created by yerang on 2023-04-28.
//
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
int map[101][71] = {0,};
bool visited[101][71] = {0,};
bool isBong = false;
int res = 0;

int axisY[8]={-1, 1, 0, 0, -1, -1, 1, 1};
int axisX[8]={0, 0, -1, 1, -1, 1, -1, 1};


void bfs(int y, int x) {
    queue<pair<int, int>> q;
    visited[y][x] = true;
    q.push(make_pair(y, x));

    while(!q.empty()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();
        for(int i=0;i<8;i++) {
            int my = y + axisY[i];
            int mx = x + axisX[i];
            if (my < 0 || my >= n || mx < 0 || mx >= m) continue;
            // 큰 경우
            if (map[my][mx] > map[y][x]) {
                isBong = false;
            }
            // 같은 경우
            else if (map[my][mx] == map[y][x] && !visited[my][mx]) {
                visited[my][mx] = true;
                q.push(make_pair(my, mx));
            }
        }
    }
    return;
}
/*
 * 내가 이걸 왜 틀렸을까?
 *   - 한 노드로 들어가서 인접 노드에 대해 작은/같은/큰 경우 모두에 대해서 검사하고,
 *     큰 경우에도 큐에 또 삽입해서 그 노드 기준으로 보고.. 종료 시점이 정확히 없었음.
 *     봉우리를 하나라도 찾아야 끝나는 형태. 그러다가 또 max값을 갱신할 놈을 찾으면 또 봉우리가 되고.... 악순환
 *   - 게다가 visited 여부를 또 봄 ㅋㅋㅋ visited 된거면 큰지 작은지조차 구분을 안하니까
 *     주변에 큰 값이 있는데도 본인이 봉우리가 되어버림 ㅋㅌㅋㅋㅌ
 *
 * 어떻게 풀었어야 할까?
 *   - 한 노드를 기준삼아 들어가면 그 노드의 높이를 기억하고 그 노드와 같은 높이를 가지는 노드는 큐에 삽입.
 *     하나씩 팝하면서 순회할 때 현재 위치로부터 8방향에 더 큰 값이 있는지 찾음(여기서 중요한건 방문 여부와 상관 없이!!!!!!!)
 *   - 8 방향 중에 큰 값이 있으면 기준삼아 들어왔던 노드는 봉우리가 아님.
 *   - 근데 같은 값이 있으면 그 것도 봉우리 후보니깐 그 주변 노드도 검사해줘야돼서 큐에 삽입.
 *   - 위를 반복...
 *
 * 다시 풀 수 있으려면 어떻게 생각해야 될까?
 *   - Queue를 순회하는 모든 경우에 visited를 봐야하는 건 아니다를 명심하기.
 *
 * */

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
                isBong=true;
                bfs(i, j);
                if (isBong) {
                    res++;
                }
            }
        }
    }
    cout << res << endl;

    return 0;
}