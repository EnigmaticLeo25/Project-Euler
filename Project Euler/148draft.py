l=[[1],[1,1]]
r=2
s=3
for i in range(398):
    count=0
    l1=[1]
    for j in range(i+1):
        c = l[i+1][j]+ l[i+1][j+1]
        l1.append(c)
        if(c%7==0):
            count=count+1
    l1.append(1)
    l.append(l1)
    r=r+1
    print(r,len(l1)-count)
    s=s+(len(l1)-count)
import math
print(s)
s=0
c=1
a=0
cinc=0
for i in range(1,201):
    
    if(i<=7):
        s=s+i
        print(i,i)
        continue
    if(math.log(i-1,7)==int(math.log(i-1,7))):
        lo = math.log(i-1,7)
        cinc=cinc+lo
        c=cinc
        a=cinc
        s=s+a
        print(i,a)
        continue
    if(i%7==1):
        c=c+cinc
        a=c
        s=s+a
    
    else:
        a=a+c
        s=s+a
    print(i,a)
print(s)
        