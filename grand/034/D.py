from collections import deque
N = int( input())
R = deque()
for _ in range(N):
    x, y, c = map( int, input().split())
    for _ in range(c):
        R.append((x+y,x,y,c))
B = [list(map( int, input().split())) for _ in range(N)]
R = list(R)

R.sort()
ans = 0
for i in range(N):
    _,x,y,c = R[i]
    T = []
    for i in range(N):
        if B[i][2] == 0:
            continue
        T.append(( abs(x-B[i][0]) + abs(y-B[i][1]), B[i][2],i))
    T.sort()
    print(i, R[i],B)
    while c > 0:
        print(c,T)
        f, g, j = T.pop()
        if c <= g:
            B[j][2] -= c
            ans += c*f
            break
        B[j][2] = 0
        c -= g
        ans += g*f
print(ans)
