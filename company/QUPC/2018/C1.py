#from copy import deepcopy
H, W, X = map( int, input().split())
S = [['']*W]*H
I = []
U = []
for i in range(H):
    s = list( input())
    S[i] = s
    for j in range(1,W-1):
        if s[j] == 'S':
            start = (i, j)
            U.append((i,j))
        if s[j] == '@':
            I.append((i,j))
            S[i][j] = '#'

for i in range(X):
    II = I
    I = []
    for x in II:
        a, b = x
        if S[a][b-1] == 'G' or S[a][b+1] == 'G' or S[a-1][b] == 'G'  or S[a+1][b] == 'G':
            U = []
            break
        if S[a][b-1] == '.':
            S[a][b-1] = '#'
            I.append(( a, b-1))
        if S[a][b+1] == '.':
            S[a][b+1] = '#'
            I.append(( a, b+1))
        if S[a-1][b] == '.':
            S[a-1][b] = '#'
            I.append(( a-1, b))
        if S[a+1][b] == '.':
            S[a+1][b] = '#'
            I.append(( a+1, b))
ans = -1
now = 0
while U:
    UU = U
    U = []
    now += 1
    for x in UU:
        a, b = x
        if  S[a][b-1] == 'G':
            ans = now
            break
        if S[a][b+1] == 'G':
            ans = now
            break
        if S[a-1][b] == 'G':
            ans = now
            break
        if S[a+1][b] == 'G':
            ans = now
            break
        if  S[a][b-1] == '.':
             S[a][b-1] = '#'
             U.append(( a, b-1))
        if S[a][b+1] == '.':
            S[a][b+1] = '#'
            U.append(( a, b+1))
        if S[a-1][b] == '.':
            S[a-1][b] = '#'
            U.append(( a-1, b))
        if S[a+1][b] == '.':
            S[a+1][b] = '#'
            U.append((a+1, b))
    if ans >= 0:
        break    
print(ans)
