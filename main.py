checkinput = [1,2,1]
checkduplicate = []
i = 0
j=0
k=0
length=len(checkinput)
while i < length:
    while j<length-1:

        if checkinput[i] == checkinput[j+1]:
           checkduplicate.append(checkinput[i])
           k+=1
        j += 1
        # else:
        # checkduplicate[i]=checkinput[i]

    i += 1
    j=0
    k=0

print(checkduplicate)