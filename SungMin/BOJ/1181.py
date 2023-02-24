n = int(input())
s = set()
for i in range(n):
    a = input()
    s.add(a)
li = list(s)
li.sort()
li.sort(key = len)

for i in li:
    print(i)