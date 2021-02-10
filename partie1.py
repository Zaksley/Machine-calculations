import math
import numpy as n;
import matplotlib.pyplot as p



print("PARTIE 1")

def rp(x, p):

    if ( x== 0):   return 0;

    exposant = 0
    while x > 1 or x < -1:
        x /= 10
        exposant += 1

    test=exposant

    while x < 0.1 and x > -0.1:
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
    for i in range(1, pow(10, prec), 2):
        sum += 1/(i*(i+1))
    return sum


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


# Valeurs intéressantes: 
"""
lx =n.linspace(-10,10,100)  ou 200
y = 5
prec = 3

y=0 special ?! 

"""

"""
lx =n.linspace(-10,10,100)
y = 5.75
prec = 3


fx = [erreur_add(x, y, prec) for x in lx]



p.plot(lx, fx)  # on utilise la fonction sinus de Numpy
p.ylabel('fonction sinus')
p.xlabel("l'axe des abcisses")
p.show()  """


print()


# Question 5
test = 7

    # Erreur relative
for i in range(1, 7):
    prec = i
    value = erreur_add(calcul_log(prec), n.log(2), prec)
    print("Erreur relative avec une precision " + str(prec) + " : " + str(value))

# Affichage de la précision du calcul de log en comparaison avec la vraie valeur de log

value = calcul_log(prec)

lx = [i for i in range(1, prec)]


p.plot(lx, [calcul_log(prec) for prec in lx])  # on utilise la fonction sinus de Numpy
p.plot(lx, [n.log(2) for x in lx])
p.yscale("log")
p.ylabel("l'axe des ordonnées")
p.xlabel("l'axe des abcisses")
p.show()  
