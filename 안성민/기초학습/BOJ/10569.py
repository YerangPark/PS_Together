T = int(input())
for i in range(T):
    v, e = map(int, input().split())

    cnt = e-v+ 2
    print(cnt)