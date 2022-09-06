N = int(input())
nums = list(map(int, input().split()))

nums_max = nums[0]
nums_min = nums[0]

for i in range(N):
    if nums[i] > nums_max:
        nums_max = nums[i]
    elif nums[i] < nums_min:
        nums_min = nums[i]
        
print(nums_min, nums_max)

