N = int( input())
S = input()
Q = int( input())
K = list( map( int, input().split()))
M = [0]*N
m = 0
D = [0]*(N+1)
C = [0]*(N+1)
for i in range(N):
    if S[i] == 'D':
        D[i+1] = D[i] + 1
        C[i+1] = C[i]
        M[i+1] = M[i]
    elif S[i] == 'C':
        C[i+1] = C[i] + 1
        D[i+1] = D[i]
        M[i+1] = M[i]
    elif S[i] == 'M':
        M[i+1] = M[i] + 1
        C[i+1] = C[i]
        D[i+1] = D[i]
for _ in range(Q):
    k = int( input())
    ans = 0
    for i in range(N-k+1):
        ans += 
