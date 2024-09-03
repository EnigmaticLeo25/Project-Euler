def bouncy(x):
    flag=0
    l = str(x)
    t = 0
    for i in range(len(l)-1):
        a = l[i]
        b = l[i+1]
        if(a==b):
            continue
        else:
            if(a>b):
                flag=0
                
            else:
                flag=1
            t=i
            break
        
    for i in range(t+1,len(l)-1):
        s1 = l[i]
        s2 = l[i+1]
        if(s1==s2):
            continue
        if(s1>s2 and flag==1):
            return True
        if(s1<s2 and flag==0):
            return True
    return False
c=0
for i in range(1000000,10000000):
    if(bouncy(i)):
        c+=1
    
print(c)        
print(bouncy(123632))  
        
            