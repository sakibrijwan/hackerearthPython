inp=input()
word = []
word = list(inp)


length = len(word)
i = 0
while i < length:
    if word[i].isupper():
        word[i]=word[i].lower()

    else:
       word[i]=word[i].upper()
    i += 1

str=''.join(word)
print(str)
