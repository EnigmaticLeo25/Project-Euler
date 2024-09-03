import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
c='1111111111'
'''for i in range(100):
    c=c +'1111111111'
    c=int(c)
    print(c,end="   ")
    count=0
    for j in range(11,int(math.sqrt(c))+1,10):
        if(c%j==0):
            if(prime(j)):
                count+=1
                print(j,end=" ")
                if(count==15):
                    break
    print(" ")
    c=str(c)'''
l=[]
for i in range(3,100000,2):
    if(prime(i)):
        l.append(i)


c=0
for i in range(10000):
    c=c*10+1

s=0
count=0
for i in l:
    if(c%i==0):
        count+=1
        print(i,count)
        s=s+i
print(s)