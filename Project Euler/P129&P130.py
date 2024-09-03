import math

def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True

count=0
s=0
for i in range(1,100000,2):
    if(i%5!=0):
        c=1
        while(c%i!=0):
            c=c*10+1
        a = len(str(c))
        if((i-1)%a==0):
            if(not prime(i)):
                count=count+1
                print(i,a,count)
                s=s+i
                if(count==25):
                    break
                
print(s)               