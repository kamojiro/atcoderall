from collections import defaultdict
N = int( input())
ans = 50
X = [ tuple( map( int, input().split())) for _ in range(N)]
X.sort(reverse=True)
for i in range(N-1):
    for j in range(i+1,N):
        if i == j:
            continue
        p = X[i][0] - X[j][0]
        q = X[i][1] - X[j][1]
        d = defaultdict( int)
        now = 0
        for k in range(N):
            if d[X[k]] == 0:
                now += 1
            d[(X[k][0], X[k][1])] = 1
            d[(X[k][0]+p, X[k][1]+q)] = 1
            d[(X[k][0]-p, X[k][1]-q)] = 1
        if now < ans:
            ans = now
if N == 1:
    ans = 1
print(ans)
