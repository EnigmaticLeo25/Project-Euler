f = open("0042_words.txt","r")
str = f.read()
print(str)
l = str.split(",")
print(l)

r=[]
for i in l:
    i=i.strip('"')
   
    r.append(i)
print(r)
t=[]
for i in range(26):
    a = i*(i+1)/2
    t.append(int(a))
t.remove(0)
print(t)

count=0
for i in r:
    s=0
    for j in i:
        a=ord(j)-64
        s=s+a
    if(s in t):
        count+=1
print(count)
