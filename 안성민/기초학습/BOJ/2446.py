N = int(input())

for i in range(N):
    a = ' ' * i + '*' * ((2 * N) - (2 * i + 1))
    print(a)
for i in range(2, N+1):
    b = ' ' * (N - i) + '*' * (2 * i - 1)
    print(b)