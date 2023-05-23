n = int(input())
day = list(map(int, input().split()))

jun_m = n
jun_c = 0
sung_m = n
sung_c = 0

arr = []

for i in day:
    jun_c += jun_m // i
    jun_m = jun_m % i
    
    arr.append(i)
    if len(arr) >= 4:
        if arr[0] > arr[1] > arr[2]:
            sung_m = sung_m % i
            sung_c += sung_m // i
        elif arr[0] < arr[1] < arr[2]:
            sung_m += sung_c*i
            sung_c = 0
        arr.pop(0)
if jun_m + jun_c*day[-1] > sung_m + sung_c*day[-1]:
    print('BNP')
elif jun_m + jun_c*day[-1] < sung_m + sung_c*day[-1]:
    print('TIMING')
else:
    print('SAMESAME')