# import sys
# input = sys.stdin.readline
# from collections import deque
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# graph = [[] for _ in range(n+1)]

# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
# visited = [0] *(n+1)
# count = [0] * (n+1)

# def bfs(a):
#     queue = deque()
#     queue.append(a)
#     visited[a] = 1

#     while queue:
#         x = queue.popleft()
#         for i in graph[x]:
#             if visited[i] == 0:
#                 visited[i] = 1
#                 count[i] = count[x] + 1
#                 queue.append(i)

# bfs(a)

# if count[b] > 0:
#     print(count[b])
# else:
#     print(-1)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
count = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(a):
    visited[a] = 1
    for i in graph[a]:
        if visited[i] == 0:
            visited[i] = 1
            count[i] = count[a] + 1 
            dfs(i)

dfs(a)
if count[b] > 0:
    print(count[b])
else:
    print(-1)