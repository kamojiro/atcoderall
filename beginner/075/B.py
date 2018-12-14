def number(B, i, j):
    bob = 0
    if i-1 != -1:
        for k in range(max(0,j-1),min(W-1,j+1)+1):
            if B[i-1][k] == '#':
                bob += 1
    if j-1 != -1:
        if B[i][j-1] == '#':
            bob += 1
    if j+1 != W:
        if B[i][j+1] == '#':
            bob += 1
    if i+1 != H:
        for k in range(max(0,j-1),min(W-1,j+1)+1):
            if B[i+1][k] == '#':
                bob += 1
    return bob

H, W = map( int, input().split())
B = [input() for _ in range(H)]
S = ['' for _ in range(H)]
for i in range(H):
    for j in range(W):
        if B[i][j] == '#':
            S[i] += '#'
        else:
            S[i] += str(number(B,i,j))
for i in range(H):
    print(S[i])
