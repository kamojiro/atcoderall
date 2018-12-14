N, M, A, B = map( int, input().split())
A, B = min(A,B), max(A,B)
V = [0]*N
for _ in range(M):
    L, R = map( int, input().split())
    for i in range(L-1,R):
        V[i] = 1
S = sum(V)
print(S*A + (N-S)*max(A,B))
