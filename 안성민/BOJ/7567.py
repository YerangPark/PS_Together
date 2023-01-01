s = list(input())

sum = 10

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        sum += 5
    elif s[i] != s[i-1]:
        sum += 10
print(sum)