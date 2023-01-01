N = int(input())

for i in range(N):
    li = list(map(int, input().split()))
    cnt = 0
    for j in li[1:]:
        avg = sum(li[1:]) / li[0]
        if j > avg:
            cnt += 1
    rate = cnt / li[0]*100
    print(f'{rate:.3f}%')

