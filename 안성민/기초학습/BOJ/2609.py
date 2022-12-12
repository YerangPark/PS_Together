a, b = map(int, input().split())

arr = []

for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        arr.append(i)
arr.sort()
print(arr[-1])

for i in range(1, 10001):
    answer = arr[-1] * a // arr[-1] * b // arr[-1]
print(answer)