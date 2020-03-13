#import sys
#input = sys.stdin.readline
import heapq
def main():
    H, W, T = map( int, input().split())
    S = [ list( input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'S':
                sx, sy = i, j
            if S[i][j] == 'G':
                gx, gy = i, j
    l = 1
    r = T
    while r-l > 1:
        m = (l+r)//2
        q = [(0, sx, sy)]
        B = [[-1]*W for _ in range(H)]
        while q:
            t, x, y = heapq.heappop(q)
            if x == gx and y == gy:
                time = t
                break
            if B[x][y] != -1:
                continue
            B[x][y] = t
            if x > 0:
                if B[x-1][y] == -1:
                    if S[x-1][y] == '.' or S[x-1][y] == 'G':
                        heapq.heappush(q, (t+1, x-1, y))
                    else:
                        heapq.heappush(q, (t+m, x-1, y))
            if x < H-1:
                if B[x+1][y] == -1:
                    if S[x+1][y] == '.' or S[x+1][y] == 'G':
                        heapq.heappush(q, (t+1, x+1, y))
                    else:
                        heapq.heappush(q, (t+m, x+1, y))
            if y > 0:
                if B[x][y-1] == -1:
                    if S[x][y-1] == '.'  or S[x][y-1] == 'G':
                        heapq.heappush(q, (t+1, x, y-1))
                    else:
                        heapq.heappush(q, (t+m, x, y-1))
            if y < W-1:
                if B[x][y+1] == -1:
                    if S[x][y+1] == '.'  or S[x][y+1] == 'G':
                        heapq.heappush(q, (t+1, x, y+1))
                    else:
                        heapq.heappush(q, (t+m, x, y+1))
        if time <= T:
            l = m
        else:
            r = m

    print(l)
        
if __name__ == '__main__':
    main()
