N = int( input())
W = list( map( int, input().split()))
S = sum(W)
ans = S
now = 0
for i in range(N):
    now += W[i]
    if abs(S - now*2) < ans:
        ans = abs(S-now*2)
print(ans)
