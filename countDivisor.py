inp= [None]*10
inp=input().split()
len=len(inp)
result=[0]*len

i=0
v1=int(inp[0])
v2=int(inp[1])
v3=int(inp[2])
if v1==v2:
    i=0
else:

    while v1<=v2:
        if v1%v3==0:
          i+=1
        v1+=1

print(i)
