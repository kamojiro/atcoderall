#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    B = [ int( input()) for _ in range(N-1)]
    E = [[] for _ in range(N+1)]
    for i in range(N-1):
        E[B[i]].append(i+2)
    D = [0]*(N+1)
    d = deque([1])
    q = deque([])
    while d:
        v = d.popleft()
        q.appendleft(v)
        for w in E[v]:
            D[w] = D[v] + 1
            d.append(w)
    ANS = [0]*(N+1)
    for v in q:
        if len(E[v]) == 0:
            ANS[v] = 1
        elif len(E[v]) == 1:
            ANS[v] = 2*ANS[E[v][0]]+1
        else:
            ANS[v] = max([ ANS[w] for w in E[v]]) + min([ ANS[w] for w in E[v]]) + 1
    print(ANS[1])
    
if __name__ == '__main__':
    main()
