import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    visited[x][y] = 1
    global trigger
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] > graph[x][y]:
                trigger = False
            if graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0:
                dfs(nx, ny)



cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and visited[i][j] == 0:
            trigger = True
            dfs(i, j)
            
            if trigger == True:
                cnt += 1
print(cnt)
