H, W = map( int, input().split())
A = [ input() for _ in range(H)]
B = [ [-1]*W for _ in range(H)]
q = []
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            B[i][j] = 0
            q.append(i*W + j)
while q:
    t = q.pop(0)
    h = t//W
    w = t - h*W
    #left
    if h > 0:
        if B[h-1][w] == -1:
            B[h-1][w] = B[h][w]+1
            q.append((h-1)*W+w)
    if h < H-1:
        if B[h+1][w] == -1:
            B[h+1][w] = B[h][w] + 1
            q.append((h+1)*W + w)
    if w > 0:
        if B[h][w-1] == -1:
            B[h][w-1] = B[h][w] + 1
            q.append(h*W + w-1)
    if w < W-1:
        if B[h][w+1] == -1:
            B[h][w+1] = B[h][w] + 1
            q.append((h*W+w+1))
C = [ max(B[i]) for i in range(H)]
print( max(C))
