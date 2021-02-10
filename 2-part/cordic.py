L = [0.6931471805599453, 0.0953101798043249, 0.0099503308531681, 0.0009995003330835, 0.0000999950003333, 0.0000099999500003, 0.0000009999995]

ln10 = 2.3025850929940456840179914546843642076011014886287729760333279009

import numpy as np

A=[np.arctan(2^-k) for k in range(5)]

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

def cordic_tan(x) :

    k = 0
    n = 0
    d = 1

    while (k <= 4) :
        while ( x >= A[k] ) :
            x = x - A[k]
            np = n + d*pow(10, -k)
            d = d - n*pow(10, -k)
            n = np

        k = k + 1

    return (n + x*d)/(d - x*n)

print(cordic_tan(3))
