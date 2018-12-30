from itertools import combinations
H, W = map( int, input().split())
A = [ list( input()) for _ in range(H)]
for X in combinations([i for i in range(H+W-2)], H-1):
    I = [0]*(H+W-2)
    for i in range(H-1):
        I[X[i]] = 1
    B = [ ["."]*W for _ in range(H)]
    B[0][0] = "#"
    nowx = 0
    nowy = 0
    for i in range(H+W-2):
        if I[i] == 1:
            if A[nowx+1][nowy] == "#":
                nowx += 1
        else:
            if A[nowx][nowy+1] == "#":
                nowy += 1
        B[nowx][nowy] = "#"
    if nowx == H-1 and nowy == W-1:
        break
ans = "Possible"
for i in range(H):
    for j in range(W):
        if not A[i][j] == B[i][j]:
            ans = "Impossible"

print(ans)
