f = open("0067_triangle.txt","r")
s=f.read()
print(s)

s=s.split('\n')

print(s)
s.remove('')


for i in range(len(s)):
    s[i] = s[i].split(' ')
    
print(s)

for i in range(len(s)):
    for j in range(len(s[i])):
        s[i][j]=int(s[i][j])
print(s)


for i in range(len(s)-2,-1,-1):
    for j in range(len(s[i])):
        m = max(s[i+1][j],s[i+1][j+1])
        s[i][j] = s[i][j]+m
        
for i in range(len(s)):
    print(s[i])
