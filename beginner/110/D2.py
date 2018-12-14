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
N, M = map( int, input().split())
C = primes(M)
ans = 1
if N == 1:
    print(1)
else:
    for x in C:
        for i in range(x):
            ans *= N+i
        ans //= factorial(x)
        ans = ans%Q
    print(ans)
            
