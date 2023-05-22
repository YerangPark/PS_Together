n = int(input())
cnt = 0
cow = [2] * 11

for i in range(n):
    a, b = map(int, input().split())

    if cow[a] == 2:
        cow[a] = b
    
    elif cow[a] != b:
        cow[a] = b
        cnt += 1
        
print(cnt)