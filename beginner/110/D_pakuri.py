import sys
sys.setrecursionlimit(100000)

Q = 10**9+7
N,M = list(map(int,input().split()))
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def cmb(n,r):
    if n-r < r: r = n-r
    if r == 0: return 1
    denominator = 1                       #分母
    numerator = 1                         #分子
    for i in range(r):
        numerator *= n-i
        numerator %= Q
        denominator *= i+1
        denominator %= Q
    return numerator*pow(denominator, Q-2, Q)%Q


ans = 1
for val,dupes in factorize(M):
    ans *= cmb(N+dupes-1,N-1)
    ans = ans % Q
print(ans%Q)
