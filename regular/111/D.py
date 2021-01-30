#import sys
#input = sys.stdin.readline
from collections import defaultdict

def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

def main():
    N, M = map(int, input().split())
    AB = [ tuple(map(lambda x:int(x)-1,input().split())) for _ in range(M)]
    C = [(c, i) for i, c in enumerate(map(int,input().split()))]
    C.sort(key=lambda x:x[0])
    T = []
    now = 0
    S = []
    for c, i in C:
        if now < c:
            now = c
            if S:
                T.append(S)
                S = []
        S.append(i)
    T.append(S)
    E = []*N
    Edge = [[False]*N for _ in range(N)]
    right = "->"
    left = "<-"
    d = defaultdict(lambda:(1,""))
    for i, ab in enumerate(AB):
        a, b = ab
        d[(a,b)] = (i,right)
        d[(b,a)] = (i,left)
        # E[a].append(b)
        # E[b].append(a)
        Edge[a][b] = True
        Edge[b][a] = True


    Checked = [False]*N
    ANS = [""]*M
    for S in T:
        for s in S:
            Checked[s] = True
        for s in S:
            for v in range(N):
                if Checked[v]:
                    if Edge[s][v]:
                        i, direction = d[(s,v)]
                        ANS[i] = direction
        V = [i for i in range(N)]
        for s in S:
            for v in S:
                if Edge[s][v]:
                    union(V,s,v)
        W = [[] for _ in range(N)]
        for s in S:
            W[find(V,s)].append(s)
        for component in W:
            if not component:
                continue
            lc = len(component)
            if lc == 1:
                continue
            visited = [False]*N
            z = component[0]
            visited[z] = True
            for _ in range(lc):
                for w in component:
                    if visited[w]:
                        continue
                    if Edge[z][w]:
                        i, direction = d[(z,w)]
                        ANS[i] = direction
                        z = w
            i, direction = d[(z,component[0])]
            ANS[i] = direction
    print("\n".join(ANS))
if __name__ == '__main__':
    main()
