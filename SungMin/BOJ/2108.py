n = int(input())
li = []
for i in range(n):
    x = int(input())
    li.append(x)
li.sort()
cnt = []
li_sum = 0
for i in range(n):
    li_sum += li[i]
    avg = li_sum / len(li) # 산술평균
    
    cen = n//2 + 1 # 중앙값
    center = li[cen]

print()
