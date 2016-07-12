inp=input()
word = []
word = list(inp)
length=len(word)
new_word= [None]*length
i=0
while length>0:
    new_word[i]=word[length-1]
    length -= 1
    i += 1
new_word=''.join(new_word)
word=''.join(word)
if new_word==word:
    print("YES")
else:
    print("NO")

