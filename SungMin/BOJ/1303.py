import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    cnt = 1
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                queue.append((nx, ny))
    return cnt ** 2


result = 0
result2 = 0

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W' and visited[i][j] == 0:
            result += bfs(i, j)
        if graph[i][j] == 'B' and visited[i][j] == 0:
            result2 += bfs(i, j)

print(result, result2)
