from collections import deque
def main():
    H, W = map( int, input().split())
    r, c = map( lambda x: int(x)-1, input().split())
    S = [ list( input()) for _ in range(H)]
    T = [[False]*W for _ in range(H)]
    T[r][c] = True
    d = deque()
    d.append((r,c))
    
    while d:
        x, y = d.popleft()
        if x > 0:
            if not T[x-1][y]:
                if S[x-1][y] == "." or S[x-1][y] == "v":
                    T[x-1][y] = True
                    d.append((x-1,y))
        if x < H-1:
            if not T[x+1][y]:
                if S[x+1][y] == "." or S[x+1][y] == "^":
                    T[x+1][y] = True
                    d.append((x+1,y))

        if y > 0:
            if not T[x][y-1]:
                if S[x][y-1] == "." or S[x][y-1] == ">":
                    T[x][y-1] = True
                    d.append((x,y-1))

        if y < W-1:
            if not T[x][y+1]:
                if S[x][y+1] == "." or S[x][y+1] == "<":
                    T[x][y+1] = True
                    d.append((x,y+1))

    ANS = [[] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ANS[i].append("#")
            else:
                if T[i][j]:
                    ANS[i].append("o")
                else:
                    ANS[i].append("x")


    # print("\n".join( ["".join(["o" if t else "x" for t in WT]) for WT in T]))

    print("\n".join(["".join(ans) for ans in ANS]))




if __name__ == '__main__':
    main()
