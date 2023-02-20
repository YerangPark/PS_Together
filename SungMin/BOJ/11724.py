from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
result = 0

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        result += 1

print(result)