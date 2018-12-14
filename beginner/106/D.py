N, M, Q = map( int, input().split())
NN = [ [ 0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    L, R = map( int, input().split())
    for i in range(L+1):
        for j in range(R,N+1):
            NN[i][j] += 1

#ANS =  [ [ 0 for _ in range(N+1)] for _ in range(N+1)]
#for i in range(1,N+1):
#    ANS[i][N] = NN[i][N]
#for j in range(1,N+1):
#    for i in range(N-1,0,-1):
#        ANS[i][j] = ANS[i+1][j] + NN[i][j]
for _ in range(Q):
    p, q = map(int, input().split())
    print(NN[p][q])
