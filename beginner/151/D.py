import sys
input = sys.stdin.readline
from collections import deque
def dfs(B,si,sj, H, W):
    R = [-1]*(H*W)
    R[si*W+sj] = 0
    d = deque([si*W+sj])
    while d:
        p = d.popleft()
        x = p//W
        y = p%W
        t = R[x*W+y]

        if x > 0:
            if B[(x-1)*W+y] == 0:
                if R[(x-1)*W+y] == -1:
                    R[(x-1)*W+y] = t+1
                    d.append((x-1)*W+y)

        if x < H-1:
            if B[(x+1)*W+y] == 0:
                if R[(x+1)*W+y] == -1:
                    R[(x+1)*W+y] = t+1
                    d.append((x+1)*W+y)
        if y > 0:
            if B[x*W+y-1] == 0:
                if R[x*W+y-1] == -1:
                    R[x*W+y-1] = t+1
                    d.append(x*W+y-1)
        if y < W-1:
            if B[x*W+y+1] == 0:
                if R[x*W+y+1] == -1:
                    R[x*W+y+1] = t+1
                    d.append(x*W+y+1)

    return max(R)
    

def main():
    H, W = map( int, input().split())
    S = [ list( input()) for _ in range(H)]
    B = [0]*(H*W)
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                B[i*W+j] = 1
    ans = 0
#    print(dfs(B,i,j,H,W))

    for i in range(H):
        for j in range(W):
            if B[i*W+j] == 1:
                continue
            t = dfs(B, i, j, H, W)
            if t > ans:
                ans = t
    print(ans)
            
if __name__ == '__main__':
    main()
