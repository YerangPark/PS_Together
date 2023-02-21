
import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()
        a = graph[x]
        if visited[a] == 0:
            visited[a] = 1
            queue.append(a)


for i in range(t):
    n = int(input())
    graph = [0] + (list(map(int, input().split())))
    visited = [0] * (n+1)
    result = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i)
            result += 1

    print(result)