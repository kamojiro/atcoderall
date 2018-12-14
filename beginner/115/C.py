N, K = map( int, input().split())
H = [ int( input()) for _ in range(N)]
H.sort()
ans = 10**9
for i in range(N-K+1):
    if H[i+K-1] - H[i] < ans:
        ans = H[i+K-1] - H[i]
print(ans)
