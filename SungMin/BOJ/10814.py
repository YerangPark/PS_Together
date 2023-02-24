import sys
input = sys.stdin.readline
n = int(input())
li = []

for i in range(n):
    a, b = map(str, input().split())
    li.append((a, b))
li.sort(key = lambda x : int(x[0]))

for a, b in li:
    print(a, b)