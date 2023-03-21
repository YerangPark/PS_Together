import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

diff = 0

for i in range(1, n+1):
    diff += abs(arr[i-1] - i)
print(diff)