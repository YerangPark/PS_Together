cnt = 0
li = []
for i in range(4):
    a, b = map(int, input().split())
    cnt += b
    cnt -= a
    li.append(cnt)
print(max(li))
