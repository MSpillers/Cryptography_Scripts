import random,math

def pc(x,mct):
    if x %2==0:
        return 0
    ct=0 
    while(ct<mct):
        a=random.ranint(2,x-2)
        if pow(a,x-1,x) == 1:
            ct=ct+1
        else:
            return 0
        print(ct)

def nextprime(m):
    if (m%2) == 0:
        m+=1
    count=0
    while count <100:
        u = random.randrange(2,m-1)
        if pow(u,m-1,m)==1:
            count+=1
        else:
            count=0 
            m+=2
    return m