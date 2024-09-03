d=[1,2,3,4,5,6,7,8,9,0]
f=0
for i in range(1000000070,1999999999,100):
    a=i**2
    j=0
    a=str(a)
    for k in d:
        if(a[j]!=str(k)):
            break
        else:
            j=j+2
            if(j==20):
                f=1
                print(i,a)
                break
    if(f==1):
        break
    if(i%10000000==0):
        print(i)
print("first dobne")           
for i in range(1000000030,1999999999,100):
    a=i**2
    j=0
    a=str(a)
    for i in d:
        if(a[j]!=i):
            break
        else:
            j=j+2
            if(j==20):
                f=1
                print(i,a)
                break
    if(f==1):
        break
    if(i%10000000==0):
        print(i)

