from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visited = [0] * (F+1)
count = [0] * (F+1)

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    
    while queue:
        x = queue.popleft()
        if x == G:
            return count[G]
        for i in (x+U, x-D):
            if 0 < i <= F and visited[i] == 0:
                visited[i] = 1
                count[i] = count[x]+1
                queue.append(i)
    if count[G] == 0:
        return "use the stairs"

print(bfs(S))