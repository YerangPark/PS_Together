n = int(input()) # 테스트 개수

for _ in range(n):
    p = int(input()) # 선수의 수

    best = 0
    player = ''

    for _ in range(p):
        charge, name = input().split()
        charge = int(charge)
        if best < charge:
            best = charge
            player = name

    print(player)