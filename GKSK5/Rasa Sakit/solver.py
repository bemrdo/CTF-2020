from sympy import *
from Crypto.Util.number import *

n = 10817338847826400693993693310389738162087305543112487544514182469845530740105439717227
e = 13337
c = 1712742277417960630321571765396625971360509211869464293909518739909852740164342992459

from decimal import *
import math
import re

getcontext().prec = 100

def numtoASCII(number):
    parsing = hex(int(number))
    parsing = re.sub("0x", "", str(parsing))
    parsing = re.sub("L", "", str(parsing))
    start = 0
    end = 2
    decode = ""
    while end <= len(parsing):
        hexForm = "0x" + str(parsing[start:end])
        decode += chr(int(hexForm, 16))
        start += 2
        end += 2
    return decode


p, q = factorint(n)
print p
print q
phi = (p-1) * (q-1)
d = inverse(e,phi)
dec = pow(c, d, n)
print (dec)
