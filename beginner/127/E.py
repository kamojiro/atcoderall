def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

Q = 10**9+7
modinv = getInv(4*10**5)
N, M, K = map( int, input().split())
T = N*M
comb = 1
for i in range(K-2):
    comb *= T-2-i
    comb %= Q
    comb *= modinv[K-2-i]
    comb %= Q
ans = 0
for i in range(1, M):
    ans += N**2*(M-i)*i
    ans %= Q
for i in range(1, N):
    ans += M**2*(N-i)*i
    ans %= Q
ans %= Q
print( ans*comb%Q)







