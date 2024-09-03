from itertools import permutations
l=[0,1,2,3,4,5,6,7,8,9]
perm = permutations(l)
li=[]
for i in list(perm):
    s=""
    for j in i:
        s=s+str(j)
    li.append(s)



s=0
for i in li:
    a=i[1:4]
    b=i[2:5]
    c=i[3:6]
    d=i[4:7]
    e=i[5:8]
    f=i[6:9]
    g=i[7:]
    
    if(int(a)%2==0 and int(b)%3==0 and int(c)%5==0 and int(d)%7==0 and int(e)%11==0 and int(f)%13==0 and int(g)%17==0):
        print(i)
        s=s+int(i)
print(s)  
    