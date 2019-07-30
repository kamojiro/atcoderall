import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def main():
    N, M = map( int, input().split())
    E = [[] for _ in range(N)]
    W = [0]*N
    for _ in range(N-1):
        a, b = map( int, input().split())
        a, b = a-1, b-1
        E[a].append(b)
        E[b].append(a)
        W[a] += 1
        W[b] += 1
    cd = defaultdict( int)
    C = list( map( lambda x:x-1, map( int, input().split())))
    for c in C:
        cd[c] = 1
    d = deque([C[0]])
    V = [-1]*N
    V[C[0]] = 0
    while d:
        v = d.popleft()
        t = V[v]
        for w in E[v]:
            if V[w] == -1:
                V[w] = t+1
                d.append(w)
    end = C[0]
    now = 0
    for c in C:
        if V[c] > now:
            now = V[c]
            end = c
    count = 1
    V = [0]*N
    V[end] = 1
    def getNext(v):
        d = deque([v])
        while d:
            v = d.popleft()
            for w in E[v]:
                if V[w] == 0:
                    V[w] = 1
                    if cd[w] == 1:
                        return w
                    d.append(w)
        return -1
    ret = True
    v = end
    for i in range(M-1):
        v = getNext(v)
        if v == -1:
            ret = False
            break
    if ret:
        print("Yes")
    else:
        print("trumpet")
if __name__ == '__main__':
    main()
