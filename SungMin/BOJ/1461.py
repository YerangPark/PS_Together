n, m = map(int, input().split())
book = list(map(int, input().split()))

left = []
right = []
max_book = 0

for i in book:
    if i < 0:
        left.append(i)
    elif i > 0:
        right.append(i)
    
    if abs(i) > abs(max_book):
        max_book = i

left.sort()
right.sort(reverse = True)

cnt = 0

for i in range(0, len(left), m):
    if left[i] != max_book: 
        cnt += abs(left[i])

for i in range(0, len(right), m):
    if right[i] != max_book:
        cnt += right[i]

cnt *= 2

cnt += abs(max_book)
print(cnt)