N = int(input())

for i in range(N):
    a = '*' * (i + 1) + ' ' * ((2 * N) - ((2 * i) + 2)) + '*' * (i + 1)
    print(a)
for i in range(N - 1, 0, -1):
    b = '*' * i + ' ' * ((2 * N) - (2 * i)) + '*' * i
    print(b)