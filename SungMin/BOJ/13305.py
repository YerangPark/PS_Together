n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

cost_min = cost[0]
result = 0

for i in range(n-1):
    if cost_min > cost[i]:
        cost_min = cost[i]
    result += cost_min * dist[i]
print(result)