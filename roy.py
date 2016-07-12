i = 0
l = int(input())
N = int(input())
W = [None] * N
H = [None] * N
x = [None] * N
result = [None] * N
check=N

while check>0:
    x = input().split()
    check-=1
    print(x)
len=N
while len>0:
        W[i] = int(x[i])
        H[i] = int(x[i+1])
        i+=1
        len-=1
j=0
while N > 0:

        if N != 0 or N < 1000:
             if l > W[j] or l > H[j]:
                result[j] = "UPLOAD ANOTHER"

             if l <= W[j] and l <= H[j] and W[j] == H[j]:
                result[j] = "ACCEPTED"

             if l <= W[j] and l <= H[j] and W[j] != H[j]:
                result[j] = "CROP IT"
             j+=1

        N -= 1
print(result)



