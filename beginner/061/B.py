N, M = map( int, input().split())
V = [ [] for _ in range(N)]
for _ in range(M):
    a, b = map( int, input().split())
    V[a-1].append(b-1)
    V[b-1].append(a-1)
for i in range(N):
    print( len(V[i]))










