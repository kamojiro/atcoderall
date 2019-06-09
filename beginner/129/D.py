H, W = map( int, input().split())
P = [ input() for _ in range(H)]
T = [ [1]*W for _ in range(H)]
Y = [ [1]*W for _ in range(H) ]
S = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if P[i][j] == "#":
           S[i][j]  = 1
for i in range(H):
    now = 0
    cnt = 0
    for j in range(W):
        if S[i][j] == 0:
            cnt += 1
        else:
            for k in range(now, j):
                T[i][k] = cnt
            cnt = 0
            now = j+1
        if cnt > 0:
            for k in range(now, W):
                T[i][k] = cnt
            
for i in range(W):
    now = 0
    cnt = 0
    for j in range(H):
        if S[j][i] == 0:
            cnt += 1
        else:
            for k in range(now, j):
                Y[k][i] = cnt
            cnt = 0
            now = j+1
        if cnt > 0:
            for k in range(now, H):
                Y[k][i] = cnt

ans = 0
for i in range(H):
    for j in range(W):
        if ans < T[i][j] + Y[i][j]-1:
            ans = T[i][j] + Y[i][j]-1
print(ans)










