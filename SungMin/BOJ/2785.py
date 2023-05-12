n = int(input())
chain = list(map(int, input().split()))
chain.sort()
cnt = 1
x = 0

while True:
    
    chain[x] -= 1 #체인하나 빼기
    cnt += 1 #체인개수 증가
    
    if chain[x] == 0: #체인다 쓰면 인덱스증가
        x += 1
    
    if cnt + x >= n:
        break
    
print(cnt - 1)