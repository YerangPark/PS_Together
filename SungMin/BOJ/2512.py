n = int(input())
array = list(map(int, input().split()))
m = int(input())

start, end = 0, max(array)

while start<=end:
    mid = (start+end)//2
    total = 0
    for i in array:
        if i > mid:
            total += mid
        else:
            total += i
    if total > m:
        end = mid - 1
    else:
        start = mid + 1
print(end)