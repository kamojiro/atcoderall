from copy import deepcopy
from collections import deque
dy = [1,-1,0,0]
dx = [0,0,1,-1]
gy = -1
gx = -1
def bfs(B,y,x,n):
    global gy, gx, time
    BD = [['V']*W for _ in range(W)]
    BD[y][x] = 0
    Q = deque([[y,x]])
    time = 0
    while len(Q) != 0:
        R = Q.popleft()
        ty, tx = R[0], R[1]
        if B[ty][tx] == str(n):
            time = BD[ty][tx]
            gy, gx = ty, tx
            break
        for i in range(4):
            uy = ty + dy[i]
            ux = tx + dx[i]
            if uy != -1 and uy != H and ux != -1 and ux != W:
                if B[uy][ux] != 'X' and BD[uy][ux] == 'V':
                    BD[uy][ux] = BD[ty][tx]+1
                    Q.append([uy,ux])
    return gy, gx, time

H, W, N = map( int, input().split())
B = [ list(input()) for _ in range(H)]
ans = 0
sy = -1
for i in range(H):
    for j in range(W):
        if B[i][j] == 'S':
            sy, sx = i, j
            break
    if sy != -1:
        break
ans = 0
for i in range(1,N+1):
    gy, gx, time = bfs(B,sy,sx,i)
    sy, sx = gy, gx
    ans += time
print(ans)
    
