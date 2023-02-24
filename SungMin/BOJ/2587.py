li = []

for i in range(5):
    a = int(input())
    li.append(a)

li.sort()

print(sum(li)//5)
print(li[2])
