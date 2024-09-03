import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True

c=1
for i in range(3,1000000,2):
    if(prime(i)):
        c+=1
        d = ((i+1)**c + (i-1)**c)%(i**2)
        print(i,d,c)
        if(d>10**10):
            print(i)
            break


