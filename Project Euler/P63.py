c=0

for i in range(1,1000):
    for j in range(1,1000):
        a=i**j
        a=str(a)
        if(j==len(a)):
            c=c+1
            print(j,a)
print(c)