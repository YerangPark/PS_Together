from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    return cnt


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i, end= ' ')