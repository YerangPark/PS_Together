m = int(input())
n = int(input())
li = []

for i in range(m, n+1):
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:
        li.append(i)
if len(li) != 0:
    print(sum(li))
    print(li[0])
else:
    print('-1')