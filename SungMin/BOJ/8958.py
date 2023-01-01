N = int(input())

for i in range(N):
    a = input()
    s = list(a)
    sum = 0
    cnt = 1

    for i in s:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1

    print(sum)
