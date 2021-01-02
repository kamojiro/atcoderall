#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    G = [[0]*403 for _ in range(403)]
    N, X, Y = map( int, input().split())
    X += 201
    Y += 201
    for _ in range(N):
        x, y = map( lambda x: int(x)+201, input().split())
        G[x][y] = 1
    d = deque([(201,201)])
    V = [[-1]*403 for _ in range(403)]
    V[201][201] = 0
    H = W = 403
    while d:
        x, y = d.popleft()
        if G[x][y] == 1:
            continue
        c = V[x][y]
        if x == X and y == Y:
            print(c)
            return
        if x > 0:
            if V[x-1][y] == -1:
                V[x-1][y] = c+1
                d.append((x-1,y))
        if x < H-1:
            if V[x+1][y] == -1:
                V[x+1][y] = c+1
                d.append((x+1,y))
        if y > 0:
            if V[x][y-1] == -1:
                V[x][y-1] = c+1
                d.append((x,y-1))
        if y < W-1:
            if V[x][y+1] == -1:
                V[x][y+1] = c+1
                d.append((x,y+1))
        if x > 0 and y < W-1:
            if V[x-1][y+1] == -1:
                V[x-1][y+1] = c+1
                d.append((x-1,y+1))
        if x < H-1 and y < W-1:
            if V[x+1][y+1] == -1:
                V[x+1][y+1] = c+1
                d.append((x+1,y+1))
    print(-1)


if __name__ == '__main__':
    main()
