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