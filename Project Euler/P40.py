l=""
a=1
while(a<1000000):
    l = l + str(a)
    a = a + 1
    
ans1 = int(l[0])
ans2 = int(l[9])
ans3 = int(l[99])
ans4 = int(l[999])
ans5 = int(l[9999])
ans6 = int(l[99999])
ans7 = int(l[999999])

ans = ans1*ans2*ans3*ans4*ans5*ans6*ans7
print(ans)
