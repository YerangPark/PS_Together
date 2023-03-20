n = int(input())
li = list(map(int, input().split()))

li.sort()
res = sorted(li, reverse=True)

arr = []

for i in range(len(li)):
    x = li[i] + res[i]
    arr.append(x)
print(min(arr))