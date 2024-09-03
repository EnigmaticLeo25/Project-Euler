def palindrome(x):
    a=str(x)
    a1 = a[::-1]
    if(a==a1):
        return True
    return False
def bindrome(x):
    a=bin(x)
    a=a[2:]
    
    a1 = a[::-1]
    if(a==a1):
        return True
    return False

s=0
for i in range(1,1000000):
    if(palindrome(i)):
        if(bindrome(i)):
            s+=i
            print(i)

print(s)
