f=open("0022_names.txt","r")
s=f.read()
print(s)
s=s.split(',')
print(s)
for i in range(len(s)):
    s[i] = s[i].strip('"')
print(s)


s.sort()
print(s)
c=1
si=0
t=0
for i in s:
    si=0
    for j in i:
        si=si+ord(j)-64
    t=t+si*c
    c=c+1
print(t)
    