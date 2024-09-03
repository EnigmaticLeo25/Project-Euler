def con3(x):
    a=str(x)
    while(len(a)<3):
        a='0'+a
    s = int(a[0])+int(a[1])+int(a[2])
    if(s>9):
        return False
    else:
        for i in range(3,len(a)):
            s=s-int(a[i-3])
            s=s+int(a[i])
            if(s>9):
                return False
        return True
c=0
for i in range(1000000,10000000):
    if(con3(i)):
        c=c+1
        
print(c)