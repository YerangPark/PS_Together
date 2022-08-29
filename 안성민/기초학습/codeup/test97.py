h, w = map(int, input().split())
n = int(input())

v = []
for i in range(h+1):
    v.append([])
    for j in range(w+1):
        v[i].append(0)

for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        v[x][y] = 1
        if d == 0:
            y += 1
        elif d == 1:
            x += 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(v[i][j], end=' ')
    print()
            






