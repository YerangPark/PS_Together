N, K = map(int, input().split())
li = []
result = 0
div = K

for i in range(N):
    A = int(input())
    li.append(A)
    li.sort(reverse=True)

    
    
for i in li:
    if i <= K:
        result += div // i # 몫
        div %= i # 나머지
        if div == 0:
            break

print(result)