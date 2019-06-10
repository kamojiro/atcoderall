H, W = map( int, input().split())
d = dict()

S = [["#"]*(W+2)]+[ "#"+input()+"#" for _ in range(H)]+ [["#"]*(W+2)]
H += 2
W += 2
L = [[0]*(W+2) for _ in range(H+2)]
R = [[0]*(W+2) for _ in range(H+2)]
D = [[0]*(W+2) for _ in range(H+2)]
U = [[0]*(W+2) for _ in range(H+2)]
cnt = 0
for i in range(W):
    d[(0,i)] = 1
    d[(H-1,i)] = 1
for i in range(1,H-1):
    for j in range(W):
        if S[i][j] == "#":
            d[(i,j)] = 1
            cnt = 0
        else:
            d[(i,j)] = 0
            cnt += 1
            R[i][j] = cnt
            
for i in range(1,H-1):
    for j in range(W-1,-1,-1):
        if d[(i,j)] == 1:
            cnt = 0
        else:
            cnt += 1
            L[i][j] = cnt

for j in range(1,W-1):
    for i in range(H):
        if  d[(i,j)] == 1:
            cnt = 0
        else:
            cnt += 1
            D[i][j] = cnt

for j in range(1,W-1):
    for i in range(H-1,-1,-1):
        if d[(i,j)] == 1:
            cnt = 0
        else:
            cnt += 1
            U[i][j] = cnt

ans = 0
for i in range(1,H-1):
    for j in range(1,W-1):
        if ans < L[i][j] + R[i][j] + U[i][j] + D[i][j]:
            ans =  L[i][j] + R[i][j] + U[i][j] + D[i][j]
print(ans-3)
