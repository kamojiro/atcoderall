N, K = map( int, input().split())
A = list( map( int, input().split()))
now = sum( A[:K])
ans = now
for i in range(N-K):
    now += A[K+i] - A[i]
    ans += now
print(ans)
