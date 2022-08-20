T = int(input())

for i in range(T):
    S = input().split()
    R = int(S[0])
    for j in S[1]:
        for k in range(R):
            print(j,end='')
    print('')    
    
         


