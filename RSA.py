p = 7
q = 11
e = 17
n = p * q
phiN = (p-1) * (q-1)

print(f"\nRSA works correctly when the message size is smaller than n.\n\nHere the value of n is {n}\n")

print("=============================================================\n")

msg = input("Enter the message to send : ")
# m = 79
m = ""
for i in msg:
    m = m+str(ord(i))

m = int(m)

if (m >= n):
    print(f"m (message) : {m}")
    print("Value exceeds more than n!")
    exit()

print(f"p = {p} \nq = {q} \ne = {e} \nm (message) = {m} \n\nn = {n} \nΦ(N) = {phiN} ")

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

d = mod_inverse(e, phiN)
print("\nThe private key is :", d)

def encryption(e, m, n):
   return pow(m, e, n)
c = encryption(e,int(m),n)
print("\nThe encrypted message is :", c)

def decryption(c, d, n):
    return pow(c, d, n)
mm = decryption(c,d,n)
print("The decrypted value of M' :", mm)
print("The decrypted message is :", chr(mm))