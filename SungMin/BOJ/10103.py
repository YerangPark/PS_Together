n = int(input())
chang = sang = 100

for i in range(n):
    a, b = map(int, input().split())

    if a > b:
        sang -= a
    elif a < b:
        chang -= b
    else:
        continue
print(chang, sang, sep='\n')