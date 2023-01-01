n = int(input())

count = 0

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        count = max(count, 10000 + (a * 1000))
    elif a == b:
        count = max(count, 1000 + (a * 100))
    elif a == c:
        count = max(count, 1000 + (a * 100))
    elif b == c:
        count = max(count, 1000 + (b * 100))
    else:
        count = max(count, max(a,b,c) * 100)

print(count)
