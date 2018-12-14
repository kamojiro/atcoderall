N, M  = map( int, input().split())
A = [ list( map( int, input().split())) for _ in range(N)]
C = [ list( map( int, input().split())) for _ in range(M)]
for i in range(N):
    ans = 1
    x, y = A[i]
    path = abs(x-C[0][0]) + abs(y-C[0][1])
    for j in range(1,M):
        if path > abs(x-C[j][0]) + abs(y-C[j][1]):
            ans = j+1
            path = abs(x-C[j][0]) + abs(y-C[j][1])
    print(ans)










