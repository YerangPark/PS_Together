m = int(input())
n = int(input())

sum = 0
min = n

for i in range(1, 101):
    if m <= i*i and n >= i*i:
        sum += i*i
        if min > i*i:
            min = i*i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)