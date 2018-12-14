from copy import deepcopy
R, C = map( int, input().split())
sy, sx = map( int, input().split())
sy -= 1
sx -= 1
gy, gx = map( int, input().split())
gy -= 1
gx -= 1
B = [ list(input()) for _ in range(R)]
ans = 0
S = [[sy, sx]]
B[sy][sx] = '#'
Q = []
while len(S) != 0:
    T = deepcopy(S)
    ans += 1
    while len(T) != 0:
        P = T.pop()
        y, x = P[0], P[1]
        if B[max(0,y-1)][x] == '.':
            B[y-1][x] = '#'
            Q.append([y-1,x])
        if B[min(R-1,y+1)][x] == '.':
            B[y+1][x] = '#'
            Q.append([y+1,x])
        if B[y][max(x-1,0)] == '.':
            B[y][x-1] = '#'
            Q.append([y,x-1])
        if B[y][min(x+1,C-1)] == '.':
            B[y][x+1] = '#'
            Q.append([y,x+1])
    if B[gy][gx] == '#':
        break
    S = deepcopy(Q)
    Q = []
print(ans)
    
            
        
        

