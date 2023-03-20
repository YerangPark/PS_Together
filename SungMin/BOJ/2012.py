n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
cnt = 0

for i in range(1, n+1):
    cnt += abs(i - arr[i-1])
print(cnt)