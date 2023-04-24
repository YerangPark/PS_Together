from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    graph[x][y] = 0
    cnt = 1
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or ny < 1 or nx > n or ny > m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt
    

result = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

print(max(result))