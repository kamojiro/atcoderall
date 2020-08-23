#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    H, W = map( int, input().split())
    Ch, Cw = map( lambda x: int(x)-1, input().split())
    Dh, Dw = map( lambda x: int(x)-1, input().split())
    S = [ input() for _ in range(H)]
    k = 10**7
    R = [ [k]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                R[i][j] = -1
    R[Ch][Cw] = 0
    T = [ [False]*W for _ in range(H)]
    d = deque([(Ch, Cw)])
    MW = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2),(-1,-2), (-1,-1), (-1,1), (-1,2),(0,-2), (0,2), (1,-2), (1,-1), (1,1), (1,2),(2,-2), (2,-1), (2,0), (2,1), (2,2)]
    while d:
        # print(d)
        # print(R)
        x, y = d.popleft()
        if T[x][y]:
            continue
        else:
            T[x][y] = True
        magic = R[x][y]
        if x == Dh and y == Dw:
            break
        if x > 0:
            if R[x-1][y] > magic:
                R[x-1][y] = magic
                d.appendleft((x-1,y))
        if x < H-1:
            if R[x+1][y] > magic:
                R[x+1][y] = magic
                d.appendleft((x+1,y))
        if y > 0:
            if R[x][y-1] > magic:
                R[x][y-1] = magic
                d.appendleft((x,y-1))
        if y < W-1:
            if R[x][y+1] > magic:
                R[x][y+1] = magic
                d.appendleft((x,y+1))
        for a, b in MW:
            tx, ty = x+a, y+b
            if tx < 0 or tx > H-1:
                continue
            if ty < 0 or ty > W-1:
                continue
            if R[tx][ty] > magic:
                R[tx][ty] = magic+1
                d.append((tx,ty))

    if R[Dh][Dw] == k:
        print(-1)
    else:
        print(R[Dh][Dw])
        
    
if __name__ == '__main__':
    main()
