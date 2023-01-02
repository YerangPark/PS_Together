li = list(range(1, 31))

for i in range(28):
    a = int(input())
    li.remove(a)
li.sort()
print(li[0])
print(li[1])    