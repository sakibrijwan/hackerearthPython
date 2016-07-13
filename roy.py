i = 0
l = int(input())
N = int(input())
W = [None] * N
H = [None] * N
x = [None] * N
y=[None]*N
result = [None] * N
check=N
inp=N

x= input().split()

while inp-1>0:
    y=input().split()
    for w in y:
        x.append(w)

    inp-=1

lenth=len(x)
W=x[1::2]
H=x[::2]


res=N

j=0
while N > 0:

        if N != 0 or N < 1000:
             if l > int(W[j]) or l > int(H[j]):
                result[j] = "UPLOAD ANOTHER"

             if l <= int(W[j]) and l <= int(H[j]) and W[j] == H[j]:
                result[j] = "ACCEPTED"

             if l <= int(W[j]) and l <= int(H[j]) and W[j] != H[j]:
                result[j] = "CROP IT"
             j+=1

        N -= 1
index=0
for name in result:
    print(result[index])
    index += 1




