L = [0.6931471805599453, 0.0953101798043249, 0.0099503308531681, 0.0009995003330835, 0.0000999950003333, 0.0000099999500003, 0.0000009999995]

ln10 = 2.3025850929940456840179914546843642076011014886287729760333279009

import numpy as np

A=[np.arctan(2**-k) for k in range(5)]

def cordic_ln(x) :

    k = 0
    y = 0
    p = 1

    while ( k <= 6 ) :
        while ( x >= p + p*pow(10, -k) ) :
            y = y + L[k]
            p = p + p*pow(10, -k)

        k = k + 1

    return y + (x /p-1)


def ln(x) :

    k = 0
    while ( x > 10 ) :
        k = k + 1
        x = x/10

    return k*ln10 + cordic_ln(x)



def cordic_exp(x) :

    k = 0
    y = 1

    while ( k <= 6 ) :
        while ( x >= L[k] ) :
            x = x - L[k]
            y = y + y*pow(10, -k)

        k = k + 1

    return y + y*x

def exp(x) :

    k = 0

    while ( x - k*ln10 > ln10 ) :
        k = k + 1

    return cordic_exp( x - k*ln10 ) * pow(10, k)
    


#403.42879349273512260838718054338827960589989735712920261396718832
#403.42879349273403
#403.4287934926897

import numpy as np

A=[np.arctan(2**(-k)) for k in range(5)]

def arctan(x):
    k=0
    y=1
    r=0
    x_1=x
    if (x<0):
        x=-x
    elif(x>1):
        x=1/x
    while(k<=4):
        while(x<y*(2**(-k))):
            k=k+1
        if (k<5):
            xp=x-y*(2**(-k))
            y=y+x*(2**(-k))
            x=xp
            r=r+A[k]
    if (x_1<0):
        return -(r+(x/y))
    if(x_1>1):
        return (np.pi/2)-(r+(x/y))
    return (r+(x/y))
print("artan(10)",int(arctan(1)*10**12))
print(int(np.arctan(1)*10**12)-int(arctan(1)*10**12))

T_arctan=[]
for i in range(1000):
    T_arctan.append(int(np.arctan(i)*10**12)-int(arctan(i)*10**12))
print(T_arctan)


def tan(x):
    k=0
    n=0
    d=1
    x_1=x
    if ((x>(np.pi/4)) and (x<(np.pi/2))):
        x=(np.pi/2)-x
    if (x>(np.pi/2)):
        while (x>np.pi):
            x=x-np.pi
        x=np.pi-x
    while(k<=4):
        while(x>=A[k]):
            x=x-A[k]
            mp=n+d*(2**(-k))
            d=d-n*(2**(-k))
            n=mp
        k=k+1
    if ((x_1>(np.pi/4)) and (x_1<(np.pi/2))):
    	return 1/((n+x*d)/(d-x*n))
    if (x_1>(np.pi/2)):
    	return -(n+x*d)/(d-x*n)

    return (n+x*d)/(d-x*n)
print("pour tant")
print(tan(1))
print(np.tan(1))

T_tan=[]
for i in range(1000):
    T_tan.append(int(np.tan(i)*10**12)-int(tan(i)*10**12))
print(T_tan)

