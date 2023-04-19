from collections import deque
n, k = map(int, input().split())

cnt = [0] * (100000+1)
visited = [0] * (100000+1)
def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    
    while queue:
        x = queue.popleft()
        if x == k:
            return cnt[x]
        for i in (x+1, x-1, x*2):
            if 0<= i <= 100000 and visited[i] == 0:
                cnt[i] = cnt[x]+1
                queue.append(i)


print(bfs(n))