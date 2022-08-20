T = int(input())
for i in range(T):
    ans = input().split()
    res = float(ans[0])
    for j in range(1, len(ans)):
        if ans[j] == '@':
            res *= 3
        elif ans[j] == '%':
            res += 5
        elif ans[j] == '#':
            res -= 7
    print("%0.2f" %res)

