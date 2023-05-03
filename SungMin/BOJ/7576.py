from collections import deque
m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))            

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()
# result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
#         if graph[i][j] > result:
#             result = graph[i][j]
# print(result-1)
result = max(map(max, graph))
print(result-1)