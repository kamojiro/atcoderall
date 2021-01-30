#import sys
#input = sys.stdin.readline
# from collections import deque
def main():
    N = int( input())
    AB = [ tuple(map( lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    Q = int( input())
    A = []
    B = []
    TEX = [ tuple(map( int, input().split())) for _ in range(Q)]
    E = [[] for _ in range(N)]
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
        A.append(a)
        B.append(b)
    before = [-1]*N
    visited = [False]*N
    turn = []
    d = [0]
    while d:
        v = d.pop()
        if visited[v]:
            continue
        turn.append(v)
        visited[v] = True
        for w in E[v]:
            if not visited[w]:
                d.append(w)
                before[w] = v
    # print(turn)
    # print(before)
    tt = [0]
    now = 0
    for v in turn[1:]:
        if before[v] == now:
            now = v
            tt.append(v)
            continue
        while before[v] != now:
            if now == 0:
                break
            now = before[now]
            tt.append(now)
            # print(now)
        tt.append(v)
        now = v
    v = before[turn[-1]]
    while v != -1:
        tt.append(v)
        v = before[v]
    # print(tt)
    TRUE = [[] for _ in range(N)]
    FALSE = [[] for _ in range(N)]
    now = [False]*(Q)
    
    for i, tex in enumerate(TEX):
        t,e,x = tex
        e -= 1
        if t == 1:
            TRUE[A[e]].append((i,x))
            FALSE[B[e]].append((i,x))
        else:
            TRUE[B[e]].append((i,x))
            FALSE[A[e]].append((i,x))
    s = 0
    ANS = [0]*N
    for v in tt:
        for i,x in TRUE[v]:
            if not now[i]:
                now[i] = True
                s += x
        for i,x in FALSE[v]:
            if now[i]:
                now[i] = False
                s -= x
        if ANS[v] < s:
            ANS[v] =s
    for v in tt:
        for i,x in TRUE[v]:
            if not now[i]:
                now[i] = True
                s += x
        for i,x in FALSE[v]:
            if now[i]:
                now[i] = False
                s -= x
        if ANS[v] < s:
            ANS[v] =s

    print("\n".join(map(str, ANS)))
        
    
        
        
if __name__ == '__main__':
    main()
