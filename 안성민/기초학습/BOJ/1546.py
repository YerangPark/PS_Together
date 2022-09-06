N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)

arr = []
for i in score_list:
    arr.append(i / max_score * 100)

print(sum(arr)/N)
