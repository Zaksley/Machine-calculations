import math

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


value = rp(10.235673, 6)
print(value)


