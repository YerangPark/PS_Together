T = int(input())
best = 0
Name = ''

for i in range(T):
    N = int(input())
    for j in range(N):
        name, cnt = input().split()
        cnt = int(cnt)
        if best < cnt:
            best = cnt
            Name = name
    print(Name)
