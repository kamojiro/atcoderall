N, K = map( int, input().split())
R = list( map( int, input().split()))
R.sort()
ans = 0
for i in range(N-K, N):
    ans = ( ans + R[i])/2
print( ans)
