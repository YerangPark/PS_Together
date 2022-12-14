N = int(input())
answer = 0
for i in range(N+1):
    for j in range(i, N+1):
        sum = i + j
        answer += sum
print(answer)