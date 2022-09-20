Allnum = set(range(1, 10001))
rmvnum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    rmvnum.add(i)
Allnum = Allnum - rmvnum
for k in sorted(Allnum):
    print(k)