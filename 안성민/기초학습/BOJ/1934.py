N = int(input())

for i in range(1, N+1):
    A, B = map(int, input().split())
    a, b = A, B
    while b != 0:
        a = a%b
        a,b = b,a
    gcd = a
    lcm = A*B//a
    print(lcm)