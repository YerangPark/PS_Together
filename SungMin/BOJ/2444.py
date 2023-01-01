N = int(input())

for i in range(1, N):
    a = (' ' * (N - i) + '*' * ((2 * i) - 1))
    print(a)

for i in range(N):
    b = (' ' * i + '*' * ((2 * N) - ((2 * i) + 1)))
    print(b)