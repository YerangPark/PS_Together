n, k = map(int, input().split())
arr = []
for _ in range(n):
    li = list(map(int, input().split()))
    arr.append(li)
arr.sort(key=lambda x : (x[1], x[2], x[3]), reverse = True)

for i in range(n):
    if arr[i][0] == k:
        index = i
for i in range(n):
    if arr[index][1:] == arr[i][1:]:
        print(i+1)
        break
