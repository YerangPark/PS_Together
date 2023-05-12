n = int(input())
k = int(input())

sen = list(map(int, input().split()))

if n <= k:
    print(0)
    exit(0)

sen.sort()

dist = []
for i in range(1, len(sen)):
    x = sen[i] - sen[i-1]
    dist.append(x)

dist.sort()


for i in range(k):
    if k == 1:
        print(sum(dist))
    dist.pop()
    k -= 1