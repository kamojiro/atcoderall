N, M, Q = map( int, input().split())
NN = [ [0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    L, R = map( int, input().split())
    NN[L][R] += 1

for i in range(1,N+1):
    for j in range(1,N+1):
        NN[i][j] += NN[i][j-1]+NN[i-1][j]-NN[i-1][j-1]
for _ in range(Q):
    p, q = map( int, input().split())
    print(NN[q][q]-NN[q][p-1]-NN[p-1][q]+NN[p-1][p-1])
