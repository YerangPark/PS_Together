from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((h_x, h_y))
    
    while queue:
        x, y = queue.popleft()
        if abs(x - f_x) + abs(y - f_y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if visited[i] == 0:
                p_x, p_y = pyn[i]
                if abs(x - p_x) + abs(y - p_y) <= 1000:
                    visited[i] = 1
                    queue.append((p_x, p_y))
    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [0 for _ in range(n)]
    h_x, h_y = map(int, input().split())
    pyn = []
    for _ in range(n):
        p_x, p_y = map(int, input().split())
        pyn.append((p_x, p_y))
    f_x, f_y = map(int, input().split())
    
    bfs()