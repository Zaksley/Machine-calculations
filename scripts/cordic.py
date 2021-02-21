import numpy as np

L = [np.log(1 + pow(10,-k)) for k in range(7)]
L_base2 = [np.log(1 + pow(2,-k)) for k in range(7)]
ln10 = np.log(10)

A = [np.arctan( pow(10, (-k))) for k in range(5)]
A_base2 = [np.arctan( pow(2, (-k))) for k in range(5)]

################### CORDIC ln ##################

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

################### CORDIC ln base2 ##################

def cordic_ln_base2(x) :

    k = 0
    y = 0
    p = 1

    while ( k <= 6 ) :
        while ( x >= p + p*pow(2, -k) ) :
            y = y + L_base2[k]
            p = p + p*pow(2, -k)

        k = k + 1

    return y + (x /p-1)


def ln_base2(x) :

    k = 0
    while ( x > 10 ) :
        k = k + 1
        x = x/10

    return k*ln10 + cordic_ln_base2(x)


################### CORDIC exp ##################

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

################### CORDIC exp base2 ##################

def cordic_exp_base2(x) :

    k = 0
    y = 1

    while ( k <= 6 ) :
        while ( x >= L_base2[k] ) :
            x = x - L_base2[k]
            y = y + y*pow(2, -k)

        k = k + 1

    return y + y*x

def exp_base2(x) :

    k = 0

    while ( x - k*ln10 > ln10 ) :
        k = k + 1

    return cordic_exp_base2( x - k*ln10 ) * pow(2, k)

################### CORDIC arctan ##################

def cordic_arctan(x) :

    k = 0
    y = 1
    r = 0

    while ( k <= 4 ) :
        while ( x < y*pow(10, -k) ) :
           k = k + 1
           if ( k >= 5) :
               return r + (x/y)

        xp = x - y*pow(10, -k)
        y = y + x*pow(10, -k)
        x = xp
        r = r + A[k]

    return r + (x/y)

def arctan(x) :

    if ( x < 0 ) :
        x = -x

    if ( x > 1 ) :
        return np.pi/2 - cordic_arctan(1/x)

    return cordic_arctan(x)

################### CORDIC arctan base2 ##################


def cordic_arctan_base2(x) :

    k = 0
    y = 1
    r = 0

    while ( k <= 4 ) :
        while ( x < y*pow(2, -k) ) :
           k = k + 1
           if ( k >= 5) :
               return r + (x/y)

        xp = x - y*pow(2, -k)
        y = y + x*pow(2, -k)
        x = xp
        r = r + A_base2[k]

    return r + (x/y)

def arctan_base2(x) :

    if ( x < 0 ) :
        x = -x

    if ( x > 1 ) :
        return np.pi/2 - cordic_arctan_base2(1/x)

    return cordic_arctan_base2(x)


################### CORDIC tan  ##################

def cordic_tan(x) :

    k = 0
    n = 0
    d = 1

    while ( k <= 4 ) :
        while ( x >= A[k] ) :
            x = x - A[k]
            np = n + d*pow(10, (-k))
            d = d - n*pow(10, (-k))
            n = np
            
        k = k + 1
        
    return (n + x*d)/(d - x*n)
    

def tan(x) :

    x = x%np.pi

    if ( x == np.pi/2) :
        return None
    
    if ( x > np.pi/2 and np.pi - x > np.pi/4) :
        return - 1/cordic_tan( np.pi/2 - np.pi + x)
    if ( x < np.pi/2 and np.pi - x > np.pi/4 ) :
        return 1/cordic_tan(np.pi/2 - x)
        
    return cordic_tan(x)

################### CORDIC tan base2 ##################

def cordic_tan_base2(x) :

    k = 0
    n = 0
    d = 1

    while ( k <= 4 ) :
        while ( x >= A_base2[k] ) :
            x = x - A_base2[k]
            np = n + d*pow(2, (-k))
            d = d - n*pow(2, (-k))
            n = np
            
        k = k + 1
        
    return (n + x*d)/(d - x*n)
    

def tan_base2(x) :

    x = x%np.pi

    if ( x == np.pi/2) :
        return None
    
    if ( x > np.pi/2 and np.pi - x > np.pi/4) :
        return - 1/cordic_tan_base2( np.pi/2 - np.pi + x)
    if ( x < np.pi/2 and np.pi - x > np.pi/4 ) :
        return 1/cordic_tan_base2(np.pi/2 - x)
        
    return cordic_tan_base2(x)


################### Tests ##################

import matplotlib.pyplot as plt

min_range = 0
max_range = 1000

ecart_atan = [ np.abs(arctan(i) - np.arctan(i)) for i in range(min_range, max_range) ]
ecart_atan_base2 = [ np.abs(arctan_base2(i) - np.arctan(i)) for i in range(min_range, max_range) ]

axe_x = [i for i in range(min_range, max_range)]

plt.plot(axe_x, ecart_atan_base2, 'b')
plt.plot(axe_x, ecart_atan, 'r')

plt.ylabel('écart relatif entre CORDIC et numpy pour arctan')
plt.xlabel('x')
plt.legend(('CORDIC base 2', 'CORDIC base 10'))
plt.show()

