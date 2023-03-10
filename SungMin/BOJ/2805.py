n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = max(array)

while start<=end:
    mid = (start+end)//2
    total = 0
    for i in array:
        if mid < i:
            total += i-mid
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)