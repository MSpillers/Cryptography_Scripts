from eu_ext import modinv

#Finding points on an Elliptic Curve over Zp
def isx(p,a,b,x):
    t=(pow(x,3,p)+a*x +b)%p

    if(t==0):
        return [0,0]
    #checks if quadratic residue
    if pow(t,(p-1)//2,p) == 1:
        y=pow(t,(p+1)//4,p)
        return [y,-y%p]
    else:
        return [100,-100]

#Python function for adding and doubling points 
def padd(p,a,b,x1,y1,x2,y2):
    if x1==p and y1==p:
        return [x2,y2]
    elif x2==p and y2==p:
        return [x1,y1]
    elif x1==x2 and y1==-y2%p:
        return p,p
    elif x1==x2 and y1==y2:
        s=(3*x1*x1+a)*modinv(2*y1,p)%p
        x3=(s*s-2*x1)%p
        y3=(s*(x1-x3)-y1)%p
        return [x3,y3]
    else:
        s=(y2-y1)*(modinv((x2-x1),p))%p
        x3=(s*s-x1-x2)%p
        y3=(s*(x1-x3)-y1)%p
        return [x3,y3]

#Point Multiplication - n is the possible order of the group - find repeats
def pmul(p,a,b,x,y,n):
    xx= bin(n)
    tx = x
    ty = y
    for i in range(3,len(xx)):
        [tx,ty] =padd(p,a,b,tx,ty,tx,ty)
        if xx[i]=='l':
            [tx,ty]=padd(p,a,b,x,y,tx,ty)
    return [tx,ty]

#prints all points in a curve with parameters p,a,b
def epoints(p,a,b):
    u=(p-1)//2
    v=(p+1)//4
    for x in range (0,p):
        Y=(x*x*x+a*x+b)%p
        if Y==0:
            print(x,0)
        Z=pow(Y,u,p)%p
        if (Z==1):
            y=pow(Y,v,p)%p
            print(x,y,x,-y%p)