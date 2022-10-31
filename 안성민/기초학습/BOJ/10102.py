n = int(input())
li = list(input())

a = 0
b = 0

for i in li:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
elif a == b:
    print('Tie')