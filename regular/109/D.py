from collections import deque

import sys
input = sys.stdin.readline

def direction(ax,ay,bx,by,cx,cy):
    bx -= ax
    by -= ay
    cx -= ax
    cy -= ay
    J = [[(0,1),(1,0)], [(1,0),(0,-1)], [(-1,0),(0,1)], [(-1,0),(0,-1)]]
    for i, j in enumerate(J):
        if ((bx,by) in j) and ((cx,cy) in j):
            return i
    

def solve(around,ax,ay,bx,by,cx,cy):
    px, py = 0, 0
    qx, qy = 1, 0
    rx, ry = 0, 1
    if abs(ax-bx) + abs(ay - by) == 2:
        ax, cx = cx, ax
        ay, cy = cy, ay
    elif abs(ax-cx) + abs(ay-cy) == 2:
        ax, bx = bx, ax
        ay, by = by, ay
    #あとで判定
    direc = direction(ax,ay,bx,by,cx,cy)
    ans = 0
    if abs(px-ax) > 2 and abs(py-ay) > 2:
        m = min(abs(px-ax), abs(py-ay))
        d = m-2
        ans += dm*6
        if ax > 0:
            if ay > 0:
                ax -= d
                ay -= d
            else:
                ax -= d
                ay += d
        else:
            if ay > 0:
                ax += d
                ay -= d
            else:
                ax += d
                ay += d

    if abs(px-ax) > 2:
        m = abs(px-ax)
        d = m-2
        ans += dm*4
        if ax > 0:
            if ay > 0:
                ax -= d
            else:
                ax -= d
        else:
            if ay > 0:
                ax += d
            else:
                ax += d

    if abs(py-ay) > 2:
        m = abs(py-ay)
        d = m-2
        ans += dm*4
        if ax > 0:
            if ay > 0:
                ay -= d
            else:
                ay += d
        else:
            if ay > 0:
                ay -= d
            else:
                ay += d
    return around[ax][ay][direc]+ans

def can_move(ax, ay, )

def get_around():
    Board = [[[-1]*4 for _ in range(5)] for _ in range(5)]
    q = deque([(2,2,0)])
    Board[2][2][0] = 0
    while q:
        x, y, t = q.popleft()
        c = Board[x][y][t]
        
        
        
    
        
    
def main():
    T = int( input())
    Case = [ tuple(map(int, input().split())) for _ in range(T)]
    around = get_around()
    ANS = [ solve(around,ax,ay,bx,by,cx,cy) for ax,ay,bx,by,cx,cy in Case]
    print("\n".join(map(str,ANS)))
if __name__ == '__main__':
    main()
