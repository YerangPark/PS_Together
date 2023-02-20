from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = True

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                res[i] = res[a]+1
                visited[i] = True

bfs(a)
if res[b] > 0:
    print(res[b])
else:
    print(-1)