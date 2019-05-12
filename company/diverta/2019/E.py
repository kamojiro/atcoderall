def getInv(N):
    inv = [1] * (N + 1)
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

from collections import defaultdict
N = int( input())
A = list( map( int, input().split()))
Q = 10**9+7

F = [0]*(N+1)
for i in range(N):
    F[i+1] = F[i]^A[i]

ANS = defaultdict(lambda:0)
d = defaultdict( lambda :0)
h = defaultdict( int)
for f in F:
    if f == 0:
        for t in d:
            if ANS[t] == 0:
                ANS[t] = d[t]
                continue
            ANS[t] = (ANS[t] + ANS[t]*d[t])%Q
            h[t] += 1
        d = defaultdict( lambda :0)
    else:
        d[f] += 1
ans = 1


for a in ANS:
    ans += ANS[a]
    ans %= Q

if F[-1] == 0:
    cnt = 0
    for i in range(N+1):
        if F[i] == 0:
            cnt += 1
    modinv = getInv(cnt)
    fmodinv = [1]*(cnt+1)
    fmod = [1]*(cnt+1)

    for i in range(1,cnt+1):
        fmodinv[i] = (fmodinv[i-1]*modinv[i])%Q
        fmod[i] = (fmod[i-1]*i)%Q
    for i in range(1, cnt-1):
        ans += fmod[cnt-2]*fmodinv[i]%Q*fmodinv[cnt-2-i]%Q
        ans %= Q
        # print(fmod[cnt-2]*fmodinv[i]%Q*fmodinv[cnt-2-i]%Q)
        # print(ans)
print(ans)
