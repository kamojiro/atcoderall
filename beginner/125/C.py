from copy import deepcopy
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return(a)

def factors(n):
    Ret = []
    for i in range(2, int( n**(1/2))+1):
        if n%i == 0:
            Ret.append([])
            t = i
            while n%i == 0:
                Ret[-1].append(t)
                n //= i
                t *= i
    if n != 0:
        Ret.append([n])
    return Ret
    
N = int( input())
A = list( map( int, input().split()))
ans = A[1]
for i in range(1,N):
    ans = gcd(ans, A[i])
Fact = factors(A[0])
C = [1]
for F in Fact:
    D = deepcopy(C)
    for f in F:
        for d in D:
            C.append(d*f)
for g in C:
    check = 0
    for i in range(1,N):
        if A[i]%g != 0:
            check += 1
    if check <= 1:
        if ans < g:
            ans = g
print(ans)
