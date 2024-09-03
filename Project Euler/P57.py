n1 = 3
d1 = 2
n2 = 7
d2 = 5
s=0
for i in range(998):
    n = n1+n2*2
    d = d1+d2*2
    print("n:",n,"d:",d)
    n1 = n2
    d1 = d2
    n2 = n
    d2 = d
    if(len(str(n))>len(str(d))):
        s=s+1
print(s)
    

