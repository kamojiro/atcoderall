H, W = map( int, input().split())
A = [ list( input()) for _ in range(H)]
Flag = True
yoko = [0]*H
tate = [0]*W
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            yoko[i] = 1
            break
for j in range(W):
    for i in range(H):
        if A[i][j] == '#':
            tate[j] = 1
ANS = []
for i in range(H):
    if yoko[i] == 0:
        continue
    ans = ''
    for j in range(W):
        if tate[j] == 1:
            ans += A[i][j]
    ANS.append(ans)
for ans in ANS:
    print(ans)
    
