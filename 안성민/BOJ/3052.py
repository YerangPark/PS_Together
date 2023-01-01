arr = []
for i in range(1, 11):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))

    