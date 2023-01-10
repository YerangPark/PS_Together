N, L = map(int , input().split())
time = 0
dist = 0

for _ in range(N):
    D, R, G = map(int, input().split())
    time += D-dist
    if R > time%(R+G):
        time += (R-(time%(R+G)))
    dist = D

time += L-dist
print(time)
























