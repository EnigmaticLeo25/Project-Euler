import math
def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
l=[]
for i in range(5,1000000,2):
    if(prime(i)):
        l.append(i)
        
s=0

l1={(1,1):11,(1,3):7,(1,7):3,(1,9):9,(3,1):3,(3,3):11,(3,7):9,(3,9):7,(7,1):7,(7,3):9,(7,7):11,(7,9):3,(9,1):9,(9,3):3,(9,7):7,(9,9):11,(5,7):5}


for i in range(len(l)-1):
    p1=l[i]
    p2=l[i+1]
    a=l1[(p1%10,p2%10)]
    d=p2*a
    e = len(str(p1))
    while(d%(10**e)!=p1):
        a=a+10
        d=p2*a
    s=s+d
    print(p1,p2,d)
    
print(s) 
