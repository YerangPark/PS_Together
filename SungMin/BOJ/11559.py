from collections import deque
import sys
input = sys.stdin.readline

graph = []
for _ in range(12):
    graph.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def down():
    for i in range(6):
        top = 11
        for j in range(11, -1, -1):
            if graph[j][i] == '.':
                continue
            if top > j:
                graph[top][i] = graph[j][i]
                graph[j][i] = '.'
            top -= 1


def bfs(x, y):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    temp.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                temp.append((nx, ny))
    
def delete(temp):
    for i, j in temp:
        graph[i][j] = '.'
        



result = 0
while True:
    visited = [[0]*6 for _ in range(12)]
    flag = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visited[i][j] == 0:
                temp = []
                bfs(i, j)
            
                if len(temp) >= 4:
                    flag = 1
                    delete(temp)
    if flag == 0:
        break

    down()
    
    result += 1
print(result)