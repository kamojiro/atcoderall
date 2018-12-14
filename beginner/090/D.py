N,K = map( int, input().split())
ans = 0
if K == 0:
    ans = N**2
else:
    for b in range(K+1,N+1):
        ans += ((N+1)//b)*(b-K) + max(0, N - ((N+1)//b)*b-(K -1))
print(int(ans))









