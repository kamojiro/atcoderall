N, K = map( int, input().split())
L = [0]*K
for n in range(1,N+1):
    L[n%K] += 1
ans = 0
for a in range(1,N+1):
    if (2*a)%K == 0:
        ans += L[(K-a)%K]**2
print(ans)










