import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False 
    return True

l=[]
for i in range(3,10000,2):
    if(prime(i)):
        l.append(i)
print(l)

f=0
for i in range(9,10000,2):
    if(i in l):
        continue
    else:
        for j in l:
            a = i-j
            if(a<0):
                print("final",i)
                f=1
                break
                
            a=a/2
            if(int(math.sqrt(a))==math.sqrt(a)):
                print("fail",i)
                break

    if(f==1):
        print("final",i)
        break
        
            