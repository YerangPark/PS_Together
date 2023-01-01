T = int(input())
for i in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    answer = sum(num_list)
    print(answer)