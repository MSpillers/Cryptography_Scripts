def xgcd(u,v):
    a=u
    b=v
    prevs, s =1,0; prevt, t=0,1
    while b:
        q=a//b
        s, prevs = prevs-q*s,s
        t, prevt = prevt-q*t,t
        b, a = a%b,b
    return a,prevs,prevt

# Modular Inverse
def modinv(a,m):
    gcd,aa,mm=xgcd(a,m)
    if gcd ==1:
        return aa


def gcd(a, b):
    if a == 0 :
        return b
    return gcd(b%a, a)

def sgcd(u,v):
    while v:
        [u,v] = [v,u%v]
    return u

    

