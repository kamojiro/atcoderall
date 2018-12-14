N, T = map( int, input().split())
S = list( map( int, input().split()))
S.append(10**10)
ans = 0
now = 0
for i in range(1,N+1):
    ans += min( S[i] - now, T) #やっぱりこっちの方が遅い
    # if S[i] - now >= T:
    #     ans += T
    # else:
    #     ans += S[i] - now
    now = S[i]
print(ans)
