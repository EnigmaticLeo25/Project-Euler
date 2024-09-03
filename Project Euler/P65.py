n1=2
d1=1
n2=3
d2=1
n3=8
d3=3
c=1
sumnum=0
for i in range(97):
    if((i+1)%3==0):
        c=c+1
        n = n3*2*c + n2
        d = d3*2*c + d2
        
    else:
        n = n3 + n2
        d = d3 + d2
    n2 = n3
    d2 = d3
    n3 = n
    d3 = d
    print("term:",i+4,"num:",n,"den:",d)
    if((i+4)==100):
        s = str(n)
        for j in s:
            sumnum+=int(j)
    print(sumnum)
