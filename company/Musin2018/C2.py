N, M = map(int, input().split())
S = [ list(input()) for i in range(N)]
ans = 0
U = [ [0 for _ in range(M)] for _ in range(N)]
D = [ [0 for _ in range(M)] for _ in range(N)]
L = [ [0 for _ in range(M)] for _ in range(N)]
R = [ [0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    cnt = 0
    for j in range(M):
        if S[i][j] == '#':
            cnt = 0
        else:
            L[i][j] = cnt
            cnt += 1
    cnt = 0
    for j in range(M-1,-1,-1):
        if S[i][j] == '#':
            cnt = 0
        else:
            R[i][j] = cnt
            cnt += 1

for j in range(M):
    cnt = 0
    for i in range(N):
        if S[i][j] == '#':
            cnt = 0
        else:
            D[i][j] = cnt
            cnt += 1
    cnt = 0
    for i in range(N-1,-1,-1):
        if S[i][j] == '#':
            cnt = 0
        else:
            U[i][j] = cnt
            cnt += 1

for i in range(N):
    for j in range(M):
        ans += (L[i][j] + R[i][j])*(U[i][j]+D[i][j])
print(ans)
