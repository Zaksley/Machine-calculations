import math
import numpy as n;
import matplotlib.pyplot as p



print("PARTIE 1")
"""
def test(x, p):
    while (x > pow(10, p)):
        x /= 10
    x = round(x)
    return x"""


def rp(x, p):
    exposant = 0
    while x > 1:
        x /= 10
        exposant += 1

    test=exposant

    while x < 0.1:
        x *= 10
        exposant -= 1

    #entier
    x *= pow(10, p)
    x = round(x)
    x *= pow(10, exposant-p)

    if (x > 1):  return round(x, p-test)
    return  x

def prec_add(x, y, p):
    v1 = rp(x, p)
    v2 = rp(y, p)

    return (v1 + v2)

def prec_prod(x, y, p):
    v1 = rp(x, p)
    v2 = rp(y, p)

    return (v1 * v2)

def erreur_add(x, y, p):
    real = x+y
    computer = prec_add(x, y, p)

    return abs( (real - computer) / real )

def erreur_prod(x, y, p):
    real = x*y
    computer = prec_prod(x, y, p)

    return abs( (real - computer) / real )

def calcul_log(prec):
    sum = 0
    for i in range(1, prec):
        sum += pow(-1, i+1) / i
    return sum


prec = 4
value = calcul_log(prec)
print(value)

"""
x = 3.333
y = 451.32658
p = 4

v_real = prec_add(x, y, p)
v_computer = x + y

print(v_real)
print(v_computer)

s = erreur_add(x, y, p)
print(s)
"""

"""
x=n.linspace(-10,10,100)
y = 5
prec = 3
p.plot(x,prec_add(x, y, prec))  # on utilise la fonction sinus de Numpy
p.ylabel('fonction sinus')
p.xlabel("l'axe des abcisses")
p.show()    
"""