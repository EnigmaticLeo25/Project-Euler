import math
def abund(x):
    s=1
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            if(i!=x/i):
                s=s+i+int(x/i)
            else:
                s=s+i
    print(s)
    if(s>x):
        return 'abundant'
    else:
        return 'not'
l=[]
for i in range(12,int(28123/2)+1):
    if(abund(i)=='abundant'):
        l.append(i)
print(l)

c=[]



for i in l:
    for j in l:
        d = i+j
        c.append(d)
c=set(c)
print(c)
print(len(c))
print(28123-len(c))