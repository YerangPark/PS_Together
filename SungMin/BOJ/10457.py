import sys
sys.setrecursionlimit(2000)


def dfs(x):
    visited[x] = 1
    v = graph[x]
    if visited[v] == 0:
        dfs(v)

t = int(input())

for i in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    result = 0

    for j in range(1, n+1):
        if visited[j] == 0:
            dfs(j)
            print("j",j)
            result += 1
    print(result)