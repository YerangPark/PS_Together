li = list(map(int, input().split()))
x = 0
for i in range(5):
    x += li[i]**2
print(x%10)