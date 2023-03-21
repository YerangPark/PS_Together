x, y, w, s = map(int, input().split())

#평행으로만
result1 = (x+y) * w
#대각선으로만
if (x+y)%2 == 0:
    result2 = max(x, y) * s
#대각선 + 평행1
else:
    result2 = (max(x, y)-1) * s + w
#평행 + 대각선
result3 = min(x, y) * s + abs(x-y) * w

print(min(result1, result2, result3))
