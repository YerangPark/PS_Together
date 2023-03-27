answer = input().split('-')
arr = []

for i in answer:
    sum = 0
    div = i.split('+')
    for j in div:
        sum += int(j)
    arr.append(sum)

n = arr[0]

for i in range(1, len(arr)):
    n -= arr[i]
print(n)