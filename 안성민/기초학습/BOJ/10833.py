N = int(input())
remain = 0
sum = 0

for i in range(N):
    stu, app = map(int, input().split())
    remain = app % stu
    if remain < stu:
        sum += remain
        print(sum)
    else:
        continue
