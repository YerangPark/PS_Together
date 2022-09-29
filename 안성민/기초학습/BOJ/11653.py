N = int(input())
x = 2

while N != 1:
    if N % x != 0:
        x += 1
    else:
        N /= x
        print(x)
