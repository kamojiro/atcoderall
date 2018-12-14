from collections import Counter
from math import factorial
Q = 10**9+7
def primes(n):
    primfac = [0]
    d = 2
    while d*d <= n:
        while n%d == 0:
            primfac[-1] += 1
            n //= d
        d += 1
        if primfac[-1] != 0:
            primfac.append(0)
    if n > 1:
        if primfac[-1] == 0:
            primfac[-1] += 1
        else:
            primfac.append(1)
    return primfac
def combination(a,b):
    return ( (factorial(a)//factorial(b))//factorial(a-b))%Q
N, M = map( int, input().split())
C = primes(M)
ans = 1
if N == 1:
    print(1)
else:
    for x in C:
        ans = (ans * combination(x+N-1,N-1))%Q
    print(ans)
