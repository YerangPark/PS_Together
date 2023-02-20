# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(a, b):
#     queue = deque()
#     queue.append((a, b))

#     graph[a][b] = 0
#     count = 1

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 count += 1
#                 queue.append((nx, ny))
#     return count

# n = int(input())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# cnt = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             cnt.append(bfs(i, j))

# cnt.sort()
# print(len(cnt))
# for i in cnt:
#     print(i)


def dfs(x, y):
    global count
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n = int(input())

graph =[]
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
result = 0
count = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            cnt.append(count)
            count = 0

print(result)
cnt.sort()
for i in cnt:
    print(i)






