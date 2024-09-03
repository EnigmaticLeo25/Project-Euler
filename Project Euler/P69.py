from math import sqrt
def factors(x):
    s = 0
    for i in range(1,int(sqrt(x))+1):
        if(x%i==0):
            if(i==sqrt(x)):
                s=s+1
                continue
            s=s+2
    return s
maxval=0
max=0
for i in range(1,100):
    a = factors(i)
    if(a>=max):
        max = a
        maxval =i
print(maxval)
print(max)
s = 2*3*5*7*11*13*15*2
print(s)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

def pe69(L):
	maxn = 1
	for p in primes:
		if maxn*p > L: return maxn
		maxn *= p
	return "Buy me some more prime numbers!"

L = int(input("The maximum value of n/phi(n) for n ≤"))
print ("is", pe69(L))