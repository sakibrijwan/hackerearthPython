inp=input()
inp=int(inp)
word=[None]*inp
length=len(word)
i=0
answer=1
while i < length:
    word[i]=i+1
    i +=1
    answer=( answer *i)%(10**9+7)
print(answer)


