def checklength(n):
    if n == 0:
        return 1
    for i in range(11,-1,-1):
        if n%10**i != n:
            return i+1
Q = 10**9 + 7
def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

N = int( input())
Inv = getInv(2*10**5)
A = [ list( map( int, input().split())) for _ in range(N)]
M = [ A[i][0] for i in range(N)]
const = 1
for m in M:
    const *= m
    const %= Q
acc = 1
ans = 0
for i in range(N-1,-1,-1):
    R = A[i][1:]
    const *= Inv[M[i]]
    const %= Q
    ans += (sum(R)*acc%Q)*const%Q
    ans %= Q
    d = [0]*10
    for r in R:
        d[checklength(r)-1] += 1
    t = 0
    for j in range(10):
        t += d[j]*10**(j+1)
    t %= Q
    acc *= t
    acc %= Q
print(ans)
