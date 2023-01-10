words = []
li = []

for i in range(5):
    word = input()
    words.append(word)
    li.append(len(word))


res = ''
for i in range(max(li)):
    for j in range(5):
        if i < li[j]:
            res += words[j][i]
print(res)


