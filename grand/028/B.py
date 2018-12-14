from itertools import accumulate
N = int( input())
A = list( map( int, input().split()))
Q = 10**9 + 7
fact = [1]*(N+1)
for i in range(N):
    fact[i+1] = fact[i]*(i+1)%Q
accA = list(accumulate(A))
accf = list( accumulate(fact))
ans = 0
now = 0
if N != 2:
    ans = (accA[-2] - accA[0])%Q*pow(2,N-3,Q)*fact[N-1]%Q
    now = (accA[-2] - accA[0])%Q
for k in range(N-1):
    ans += accA[k]%Q*accf[N-k-2]%Q*k
    #pow(2,N-k-2,Q)*fact[N-k-1]%Q*fact[k+1]%Q
    ans %= Q
    ans += (accA[-1]- accA[-2-k])*accf[N-k-2]%Q*k
    #pow(2,N-k-2,Q)*fact[N-k-1]*fact[k+1]%Q
    ans %= Q
    if k != 0:
        if k == N-2:
            break
        else:
            now -= accA[-2]-accA[-3-k]
            now %= Q
            now += accA[-2]-accA[1+k]
            now %= Q
        ans += now*pow(2,N-3-k,Q)*fact[N-k-1]%Q*fact[k+1]
ans += accA[-1]*fact[N]
ans %= Q
print(ans)
