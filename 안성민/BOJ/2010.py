n = int(input())
sum = 0
for i in range(n):
    multi = int(input())
    sum += multi
answer = sum - (n-1)
print(answer)
