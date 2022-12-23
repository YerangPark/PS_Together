n = int(input())
nums = list(map(int, input().split()))
result = 0


for i in range(n):
    cnt = 0
    if nums[i] == 1:
        continue
    for j in range(1, nums[i]+1):
        if nums[i] % j == 0:
            cnt += 1
    if cnt == 2:
        result += 1
print(result)
       