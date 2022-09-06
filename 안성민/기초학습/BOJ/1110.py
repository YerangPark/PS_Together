N = int(input())
cnt = 0
n = N

while True:
    a = n % 10
    b = n // 10
    c = (a + b) % 10
    n = (a * 10) + c

    cnt += 1
    if N == n:
        break
print(cnt)    


    

    