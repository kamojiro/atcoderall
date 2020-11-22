import sys
input = sys.stdin.readline
from collections import deque
def main():
    H, W = map(int,input().split())
    C = [ list(input()) for _ in range(H)]
    A = [[-1]*W for _ in range(H)]
    Warp = [[] for _ in range(26)]
    si, sj = 0, 0
    gi, gj = 0, 0
    a = ord("a")
    for i in range(H):
        for j in range(W):
            if C[i][j] == ".":
                continue
            if C[i][j] == "#":
                A[i][j] = -2
                continue
            if C[i][j] == "S":
                si, sj = i, j
                continue
            if C[i][j] == "G":
                gi, gj = i, j
                continue
            Warp[ord(C[i][j])-a].append((i,j))
            A[i][j] = ord(C[i][j])-a
    q = deque([(si,sj)])
    B = [[-1]*W for _ in range(H)]
    B[si][sj] = 0
    used = [False]*26
    while q:
        x, y = q.popleft()
        t = B[x][y]+1
        if x > 0:
            if B[x-1][y] == -1 and A[x-1][y] != -2:
                B[x-1][y] = t
                q.append((x-1,y))
        if x < H-1:
            if B[x+1][y] == -1 and A[x+1][y] != -2:
                B[x+1][y] = t
                q.append((x+1,y))
        if y > 0:
            if B[x][y-1] == -1 and A[x][y-1] != -2:
                B[x][y-1] = t
                q.append((x,y-1))
        if y < W-1:
            if B[x][y+1] == -1 and A[x][y+1] != -2:
                B[x][y+1] = t
                q.append((x,y+1))
        if 0 <= A[x][y] <= 25:
            if used[A[x][y]]:
                continue
            used[A[x][y]] = True
            for wi, wj in Warp[A[x][y]]:
                if B[wi][wj] == -1:
                    B[wi][wj] = t
                    q.append((wi,wj))
    # print(B)
    print(B[gi][gj])

if __name__ == '__main__':
    main()
