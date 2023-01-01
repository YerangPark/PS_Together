li1 = []
li2 = []

for i in range(3):
    x, y = map(int, input().split())
    li1.append(x)
    li2.append(y)

for i in range(3):
    if li1.count(li1[i]) == 1:
        x1 = li1[i]
    if li2.count(li2[i]) == 1:
        y1 = li2[i]

print(x1, y1)
