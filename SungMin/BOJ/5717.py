while True:
    n , m = map(int, input().split())
    sum = 0
    sum += n + m
    if n == 0 and m == 0:
        break
    print(sum)