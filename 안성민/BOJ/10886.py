n = int(input())

a = 0
b = 0

for i in range(n):
    x = int(input())
    if x == 1:
        a += 1
    elif x == 0:
        b += 1

if a > b:
    print("Junhee is cute!")
elif a < b:
    print("Junhee is not cute!")