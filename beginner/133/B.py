N, D = map( int, input().split())
X = [ list( map( int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        t = 0
        for k in range(D):
            t += (X[i][k] - X[j][k])**2
        if t == ( int(t**(1/2)))**2:
            ans += 1
print(ans)
