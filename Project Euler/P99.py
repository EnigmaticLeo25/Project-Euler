import math
f=open("0099_base_exp.txt","r")
s = f.read()
s=s.split("\n")
m=0
l=0
for i in range(len(s)):
    exp = s[i]
    exp = exp.split(",")
    print(exp)
    b=int(exp[0])
    e=int(exp[1])
    v = e*math.log(b)
    if(v>m):
        m=v
        l=i+1
print(m,l)
    
