t = int(input())
cnt = 0
n = 0
li = list(map(int, input().split()))

for i in range(t):
    if li[i] == 1:
        n += 1
        cnt += n
    else:
        n = 0
print(cnt)