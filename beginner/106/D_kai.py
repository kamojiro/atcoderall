import sys
input = sys.stdin.readline
N, M, Q = map( int, input().split())
NN = [ [ 0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    L, R = map( int, input().split())
    NN[L][R] += 1
Sum = [ [ 0 ] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        Sum[i].append(Sum[i][-1]+NN[i][j])
for _ in range(Q):
    p, q = map(int, input().split())
    ans = 0
    for i in range(p,q+1):
        ans += Sum[i][q] - Sum[i][p-1]
    print(ans)
