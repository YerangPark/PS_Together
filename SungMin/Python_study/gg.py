N = int(input())
Time = list(map(int, input().split()))
Time.sort()
result = 0

for i in range(N):
    for j in range(i+1):
        result += Time[j]
print(result)