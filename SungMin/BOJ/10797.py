num = int(input())
end_num = list(map(int, input().split()))

cnt = 0
for i in range(len(end_num)):
    if end_num[i] % 10 == num:
        cnt += 1
print(cnt)