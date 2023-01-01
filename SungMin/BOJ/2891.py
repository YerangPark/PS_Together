n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
more = list(map(int, input().split()))

answer = s

broken.sort()
more.sort()

for i in range(s):
    if not more:
        break
    for j in range(r):
        if broken[i] == more[j] or broken[i] == more[j] + 1 or broken[i] == more[j] - 1:
            answer -= 1
            more[j] = -1
            break
print(answer)