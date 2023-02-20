import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
result = 0

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)



for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        result += 1

print(result)