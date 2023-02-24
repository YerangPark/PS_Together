a, b = map(int, input().split())
li = list(map(int, input().split()))

li.sort(reverse=True)

print(li[b-1])