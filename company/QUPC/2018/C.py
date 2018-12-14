from copy import deepcopy
H, W, X = map( int, input().split())
S = [['']*W]*H
for i in range(H):
    S[i] = list( input())
I = []
U = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            start = (i, j)
            U.append((i,j))
        if S[i][j] == '@':
            I.append((i,j))
            S[i][j] = '#'
for i in range(X):
    II = deepcopy(I)
    I = []
    for x in II:
        a, b = x
        if S[a][max(b-1,0)] == '.' or S[a][max(b-1,0)] == 'G':
            S[a][max(b-1,0)] = '#'
            I.append(( a, max(b-1,0)))
        if S[a][min(b+1,W-1)] == '.' or S[a][min(b+1,W-1)] == 'G':
            S[a][min(b+1,W-1)] = '#'
            I.append(( a, min(b+1,W-1)))
        if S[max(a-1, 0)][b] == '.'or S[max(a-1, 0)][b] == 'G':
            S[max(a-1, 0)][b] = '#'
            I.append(( max(a-1, 0), b))
        if S[min(a+1, H-1)][b] == '.' or S[min(a+1, H-1)][b] == 'G':
            S[min(a+1, H-1)][b] = '#'
            I.append(( min(a+1, H-1), b))
ans = -1
now = 0
while U:
    UU = deepcopy(U)
    U = []
    now += 1
    for x in UU:
        a, b = x
        if  S[a][max(b-1,0)] == 'G':
            ans = now
            break
        if S[a][min(b+1,W-1)] == 'G':
            ans = now
            break
        if S[max(a-1, 0)][b] == 'G':
            ans = now
            break
        if S[min(a+1, H-1)][b] == 'G':
            ans = now
            break
        if  S[a][max(b-1,0)] == '.':
             S[a][max(b-1,0)] = '#'
             U.append(( a, max(b-1,0)))
        if S[a][min(b+1,W-1)] == '.':
            S[a][min(b+1,W-1)] = '#'
            U.append(( a, min(b+1,W-1)))
        if S[max(a-1, 0)][b] == '.':
            S[max(a-1, 0)][b] = '#'
            U.append(( max(a-1, 0), b))
        if S[min(a+1, H-1)][b] == '.':
            S[min(a+1, H-1)][b] = '#'
            U.append(( min(a+1, H-1), b))
    if ans >= 0:
        break    
print(ans)
