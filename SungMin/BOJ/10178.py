T = int(input())
x = y = 0
for i in range(T):
    c, v = map(int, input().split())
    x = c // v
    y = c % v
    print("You get %d piece(s) and your dad gets %d piece(s)." %(x, y))