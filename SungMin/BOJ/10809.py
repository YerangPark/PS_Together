S = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(S.find(chr(i)), end=' ')
