cnt = 0
li = []
for i in range(3):
    x = list(map(int, input().split()))
    li.append(x)

for i in range(3):
    if sum(li[i]) == 3:
        print('A')

    if sum(li[i]) == 2:
        print('B')

    if sum(li[i]) == 1:
        print('C')

    if sum(li[i]) == 0:
        print('D')

    if sum(li[i]) == 4:
        print('E')
