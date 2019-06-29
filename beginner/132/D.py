Q = 10**9+7

def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

def getFactorialInv(N):
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    ret = [1]*(N+1)
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
        ret[i] = ret[i-1]*inv[i]
    return ret

def getFactorial(N):
    ret = [1]*(N+1)
    for i in range(2,N+1):
        ret[i] = ret[i-1]*i%Q
    return ret

modFact = getFactorial(2000)
modInvFact = getFactorialInv(2000)
N, K = map( int, input().split())
for i in range(1, K+1):
    if N-K+1 < i:
        print(0)
        continue
    ans = modFact[N-K+1]*modInvFact[i]%Q*modInvFact[N-K+1-i]%Q*modFact[K-1]%Q*modInvFact[K-i]%Q*modInvFact[i-1]%Q
    ans %= Q
    print(ans)
