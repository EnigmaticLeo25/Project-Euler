from math import sqrt
def sieve(x):
    l=[]
    for i in range(2,x):
        l.append(i)
    s = l[0]
    ind =0
    while(ind<sqrt(x)):
        for i in l:
            if(i%s==0):
                l.remove(i)
        ind=ind+1
        s= l[ind]
    return l
l =sieve(100000)
s=0
for i in l:
    s=s+i
print(s)