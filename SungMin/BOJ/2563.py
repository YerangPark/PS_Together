n = int(input())
li = [[0 for i in range(101)] for j in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            li[i][j] = 1

result = 0
for i in li:
    result += i.count(1)
print(result)