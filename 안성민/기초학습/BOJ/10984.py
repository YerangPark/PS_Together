t = int(input())

for i in range(t):
    sumc = 0
    sumg = 0
    n = int(input())
    for j in range(n):
        c, g = map(float, input().split())
        sumc += c
        sumg += g * c

        gpa = sumg / sumc
    print(int(sumc), round(gpa,1))