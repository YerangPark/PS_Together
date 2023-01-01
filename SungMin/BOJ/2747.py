a, b = 1, 1
li = [] 
n = int(input())

for i in range(n):
    li.append(a)
    a,b = b, a+b
print(li[-1])