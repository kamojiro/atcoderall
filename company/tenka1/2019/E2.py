def factors(z):
    ret = []
    for i in range(2, int(z**(1/2))+1):
        if z%i == 0:
            ret.append(i)
            while z%i == 0:
                z //= i
    if z != 1:
        ret.append(z)
    return ret

def eratosthenes(N):
    if N == 0:
        return []
    from collections import deque
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
    ret = []
    for i in range(N+1):
        if work[i]:
            ret.append(i)
            for j in range(2* i, N+1, i):
                work[j] = False
    return ret

N = int( input())
A = [ int( input()) for _ in range(N+1)]
Primes = eratosthenes(N)
ANS = []
F = factors( abs(A[0]))
for f in F:
    if f >= N+1:
        Primes.append(f)
for p in Primes:
    if p >= N+1:
        check = 1
        for i in range(N+1): # f が恒等的に 0 であるかどうかのチェック
            if A[i]%p != 0:
                check = 0
                break
        if check == 1:
            ANS.append(p)
    else:
        poly = [0]*(p-1)
        for i in range(N+1): # フェルマーの小定理
            poly[(N-i)%(p-1)] = (poly[(N-i)%(p-1)] + A[i])%p
        check = 0
        if sum(poly) == 0 and A[N]%p == 0: # a_0 が 0 かつ、g が恒等的に 0 であることをチェックしている
            check = 1
        if check == 1:
            ANS.append(p)
for ans in ANS:
    print(ans)
