charge = int(input())

sum = 0

for i in range(9):
    n = int(input())
    sum += n
answer = charge - sum
print(answer) 