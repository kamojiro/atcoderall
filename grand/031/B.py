N = int( input())
C = [ int( input()) for _ in range(N)]
Q = 10**9+7
D = [0]*(2*10**5+1)
D[C[0]] = 1
ans = 1
dp = [1]*(N+1)
before = C[0]
for i in range(1,N):
    if before == C[i]:
        continue
    ans, D[C[i]] = ans+D[C[i]], D[C[i]]+ans
    ans += D[C[i]]
    D[C[i]] += ans
    before = C[i]
print(ans)






