t = int(input())

for i in range(1, t+1):
    #a, b를 입력받는거
    a,b=map(int, input().split())
    #a+b를 출력하는거 Case #1: 2
    print("Case #",i ,": ",(a+b),sep='')
