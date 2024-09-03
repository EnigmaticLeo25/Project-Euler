def reverse(string):
    string = string[::-1]
    return string
def Lychrel(x):
    for i in range(50):
        rev = reverse(str(x))
        a = int(rev)
        num = x + a
        numrev = int(reverse(str(num)))
        if(numrev==num):
            return False
        x = num
    return True
s=0
print(Lychrel(10677))
for i in range(1,10000):
    if(Lychrel(i)):
        s=s+1
print(s)
