n, m = map(int, input().split())
result = []
arr = 0
for i in range(n):
    p, l = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    if (l - p) <= 0:
        result.append(arr[l-1])
    else:
        result.append(1)
result.sort()
cnt = 0

for i in result:
    m -= i
    if m < 0:
        break 
    cnt += 1
print(cnt)