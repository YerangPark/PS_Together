# N = int(input())
# dist = list(map(int, input().split()))
# cost = list(map(int, input().split()))
# result = 0
# sum = 0

# del cost[-1]
# min_c = min(cost)

# for i in range(len(cost)):
#     for j in range(len(dist)):
#         if cost[i] == min_c:
#             result += cost[i] * dist[j]
#         else:
#             sum += cost[i] * dist[j]
#             break

# print(result)
# print(sum)