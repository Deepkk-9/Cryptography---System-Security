p = 6
q = 13

a = 3
b = 10

def pubKey(p, q, a, b):
    A = ((p**a) % q)
    B = ((p**b) % q)
    return (A, B)

PkA, PkB = pubKey(p, q, a, b)

print(PkA, PkB)


def secKeyA(PkB, a, q):
    return PkB**a % q

SkA = secKeyA(PkB, a, q)

def secKeyB(PkA, b, q):
    return PkA**b % q

SkB = secKeyA(PkA, b, q)

print(SkA, SkB)
if (SkA == SkB):
    print("Data sent is correct")
else:
    print("Data sent is wrong")
