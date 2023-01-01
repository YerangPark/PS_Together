T = int(input())

for i in range(T):
    car_charge = 0
    s = int(input())
    n = int(input())
    
    for j in range(n):
        sum = 0
        q,p = map(int, input().split())
        sum = q * p
        car_charge += sum
    print(car_charge + s)