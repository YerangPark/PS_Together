import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx ,ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)