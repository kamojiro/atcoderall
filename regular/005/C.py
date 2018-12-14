from collections import deque
H, W = map( int, input().split())
B = [ list(input()) for _ in range(H)]
sy = -1
dy = [1,-1,0,0]
dx = [0,0,1,-1]
for i in range(H):
    for j in range(W):
        if B[i][j] == 's':
            sy, sx = i, j
            break
    if sy != -1:
        break
Q = deque([[sy,sx]])
DB = [[0 for _ in range(W)] for _ in range(H)]
EB = [[False for _ in range(W)] for _ in range(H)]
EB[sy][sx] = True
ans = False
while len(Q) != 0:
    y, x = Q.popleft()
    if B[y][x] == 'g':
        ans = True
        break
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if ty != -1 and ty != H and tx != -1 and tx != W:
            if B[ty][tx] == '#':
                if DB[y][x] <= 1:
                    if EB[ty][tx] == False:
                        DB[ty][tx] = DB[y][x] + 1
                        EB[ty][tx] = True
                        Q.append([ty,tx])
                    else:
                        if DB[ty][tx] > DB[y][x] + 1:
                            DB[ty][tx] = DB[y][x] + 1
                            Q.append([ty,tx])
            else:
                if EB[ty][tx] == False:
                    DB[ty][tx] = DB[y][x]
                    EB[ty][tx] = True
                    Q.appendleft([ty,tx])
                else:
                    if DB[ty][tx] > DB[y][x]:
                        DB[ty][tx] = DB[y][x]
                        Q.appendleft([ty,tx])
print('YES' if ans else 'NO')
            
            
        
    
    
