import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)
li.sort()
for i in li:
    print(i)
