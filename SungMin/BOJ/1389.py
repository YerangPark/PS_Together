from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    cnt =  [0] * (n+1)
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                cnt[i] = cnt[x] + 1
                queue.append(i)
    return sum(cnt)


result = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    if visited[i] == 0:
        result.append(bfs(i))

print(result.index(min(result))+1)