#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    H, W = map( int, input().split())
    r, c = map( lambda x: int(x)-1, input().split())
    S = [ list( input()) for _ in range(H)]
    T = [[False]*W for _ in range(H)]
    T[r][c] = True
    d = deque((r,c))
    while d:
        x, y = d.popleft()
        if S[x][y] == ">":
            if x > 0:
                if S[x-1][y] == False:
                    if S[x-1][y] == "." or S[x-1][y] == ">":
                        T[x-1][y] = True
                        d.append((x-1,y))
            continue
        if S[x][y] == "<":
            if x < H-1:
                if S[x+1][y] == False:
                    if S[x+1][y] == "." or S[x+1][y] == "<":
                        T[x+1][y] = True
                        d.append((x+1,y))
            continue
        if S[x][y] == "^":
            if y > 0:
                if S[x][y-1] == False:
                    if S[x][y-1] == "." or S[x][y-1] == "v":
                        T[x][y-1] = True
                        d.append((x,y-1))
            continue
        if S[x][y] == "v":
            if y < W-1:
                if S[x][y+1] == False:
                    if S[x][y+1] == "." or S[x][y+1] == "v":
                        T[x][y-1] = True
                        d.append((x,y-1))
            continue


if __name__ == '__main__':
    main()
