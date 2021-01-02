#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N, M, K = map( int, input().split())
    H = list( map( int, input().split()))
    C = list( map(  lambda x: int(x)-1, input().split()))
    AB = [ tuple( map( lambda x: int(x)-1, input().split())) for _ in range(M)]
    E = [[] for _ in range(N)]
    for a, b in AB:
        if H[a] < H[b]:
            E[a].append(b)
        else:
            E[b].append(a)
    # print(E)
    ANS = [-1]*N
    d = deque()
    for c in C:
        d.append(c)
        ANS[c] = 0
    while d:
        v = d.popleft()
        dist = ANS[v]+1
        for w in E[v]:
            if ANS[w] == -1:
                ANS[w] = dist
                d.append(w)
    print("\n".join(map(str, ANS)))
    
if __name__ == '__main__':
    main()
