n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

visited = [0] * (n+1)

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(visited.count(1)-1)









# from collections import deque

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# visited = [0]*(n+1)

# visited[1] = 1
# queue = deque([1])

# while queue:
#     x = queue.popleft()
#     for i in graph[x]:
#         if visited[i] == 0:
#             visited[i] = 1
#             queue.append(i)
# print(visited.count(1)-1)
















