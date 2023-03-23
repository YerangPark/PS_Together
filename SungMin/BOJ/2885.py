k = int(input())
choco = 1
cnt = 0

while choco < k:
    choco *= 2
    result = choco

while k > 0:
    if k >= choco:
        k -= choco
    else:
        choco /= 2
        cnt += 1
print(result, cnt)