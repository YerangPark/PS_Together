import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key = lambda x : (x[1], x[0]))

n = 0
cnt = 0

for i, j in arr:
    if n <= i:
        n = j
        cnt += 1
print(cnt)
