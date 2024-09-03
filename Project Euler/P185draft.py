s='''90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct'''
l = {}
s=s.split("\n")
print(s)
for i in range(len(s)):
    s[i]=s[i].split() 
    l[int(s[i][0])] = int(s[i][1][1])
    
print(l)
g=[]
for i in range(5):
    c=[]
    for j in range(10):
        c.append(j)
    g.append(c)
for i in g:
    print(i)
for i in (l.keys()):
    if(l[i]==0):
        c=0
        for j in str(i):
            g[c].remove(int(j))
            c=c+1
            
print(g)           
for i in range(l.keys()):
    a=l[i]
    for j in range(l.keys()):
        if(i!=j):
            b=l[j]
            if(b==(a-1)):
                