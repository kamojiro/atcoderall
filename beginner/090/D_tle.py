N, K = map( int, input().split())
ans = 0
for a in range(K,N+1):
    for b in range(1,a):
        if a%b >= K:
            ans += 1
    ans += N - a
print(ans)










