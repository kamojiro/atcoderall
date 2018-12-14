def getInv(N):
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

from itertools import accumulate
N = int( input())
A = list( map( int, input().split()))
Q = 10**9 + 7
fact = [1]*(N+1)
invs = getInv(N)
accI = [0]*(N+1)
for i in range(N):
    fact[i+1] = fact[i]*(i+1)%Q
    accI[i+1] = (accI[i]+invs[i+1])%Q
factN = fact[-1]
ans = 0
for i in range(N):
    C = factN*(accI[i+1] + accI[N-i]-1)*(A[i]%Q)%Q
    ans += C
    ans %= Q
print(ans)


