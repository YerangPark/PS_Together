a, b = map(int, input().split())
li1 = list(input())
li2 = list(input())
T = int(input())
li1.reverse()
total = li1 + li2

for i in range(T):
    for j in range(len(total)-1):
        if total[j] in li1 and total[j+1] in li2:
            total[j], total[j+1] = total[j+1], total[j]
            if total[j+1] == li1[-1]:
                break
print("".join(total))
