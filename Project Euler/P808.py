import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
sum=0
count=0
i=3
l=[]
while(count<50):
    if(i in l):
        i=i+2
        continue
    if(prime(i)):
        c = i**2
        s = str(c)
        crev = s[::-1]
        cint = int(crev)
        p = math.sqrt(cint)
        if(p%1==0 and cint!=c):
            if(prime(p)):
                print(i,p,c)
                sum=sum+c+cint
                count+=2
                l.append(p)
                
    i=i+2
print(sum)