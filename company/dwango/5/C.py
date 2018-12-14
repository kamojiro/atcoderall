N = int( input())
S = input()
Q = int( input())
M = [0]*N
m = 0
D = [0]*(N+1)
C = [0]*(N+1)
for i in range(N):
    if S[i] == 'D':
        D[i+1] = D[i] + 1
        C[i+1] = C[i]
    elif S[i] == 'C':
        C[i+1] = C[i] + 1
        D[i+1] = D[i]
    else:
        C[i+1] = C[i]
        D[i+1] = D[i]
    if S[i] == 'M':
        M[m] = i
        m += 1
for _ in range(Q):
    k = int( input())
    ans = 0
    for i in range(m):
        
