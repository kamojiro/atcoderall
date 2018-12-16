def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return(a)
A = [3]*4 + [5]*4 + [7]*6
s = sum(A)
# for a in A:
#     print( gcd(a, s-a))

def prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return 0
    else:
        return n

primelist = []
for i in range(2, 20000):
    if prime(i) != 0:
        primelist.append(i)

ANS = []

if N%2 == 0:
    ANS.append(2)
