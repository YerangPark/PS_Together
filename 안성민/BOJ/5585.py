n = int(input())
result = 0
arr = [500, 100, 50, 10, 5, 1]
pay = 1000 - n

for i in arr:
    result += (pay//i)
    pay = pay % i

print(result)