n = int(input())
a = list(map(int, input().split()))
d = []

for i in range(24): # 24개의 정수0을 배열에 넣음
    d.append(0)
for i in range(n): # 번호를 부를 때 마다, 그 번호 카운트 1씩증가
    d[a[i]]+=1
for i in range(1, 24): #카운트한 값을 공백을 두고 출력
    print(d[i], end=' ')