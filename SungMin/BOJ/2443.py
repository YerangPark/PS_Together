N = int(input())

for i in range(1, N+1):
    a = (' ' * (i-1) + '*' * ((2*N)-((2*i)-1)))
    print(a)