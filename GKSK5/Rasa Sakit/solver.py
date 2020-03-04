from sympy import *
from Crypto.Util.number import *

def getDec(n, e, c):
    p, q = factorint(n)
    phi = (p-1) * (q-1)
    d = inverse(e,phi)
    dec = pow(c, d, n)
    return dec

def getFlag(decs):
    flag = ''
    decs = decs.split('-')
    for x in decs:
        flag += chr(int(x))
    return flag

def main():
    n = 10817338847826400693993693310389738162087305543112487544514182469845530740105439717227
    e = 13337
    c = 1712742277417960630321571765396625971360509211869464293909518739909852740164342992459
    print getDec(n, e, c)
    decs = '71-75-83-75-123-84-52-107-95-98-49-53-52-95-109-51-110-52-104-52-110-95-82-83-52-95-53-52-107-49-84-125'
    print getFlag(decs)

if __name__ == '__main__':
    main()
