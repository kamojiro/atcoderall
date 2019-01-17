from 
Q = 10**9+7
N, M = map( int, input().split())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
G = [(0,0)]*N
R = [(0,0)]*M
for i, m in enumerate(A):
    G[i] = (m,i)
for j, m in enumerate(B):
    R[j] = (m,j)
G.sort()
R.sort()
ans = 1
A.sort()
B.sort()
for i in range(N):
    if A[i] < M*i:
        ans = 0
        break
for j in range(M):
    if B[j] < N*j:
        ans = 0
        break
IC = [0]*N
JC = [0]*N
cnt = 0
for m in range(M*N,-1,-1):
    g, i = G[0]
    r, j = R[0]
    if m == g and m == r:
        G.pop(0)
        R.pop(0)
        IC[i] = 1
        JC[i] = 1
    elif m == g:
        if IC[]
