#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    first, last = input().split()
    if first == last:
        print("0")
        print(first)
        print(last)
        return
    N = int( input())
    S = [ input() for _ in range(N)]
    S += [first, last]
    start = N
    goal = N+1
    E = [[] for _ in range(N+2)]
    L = len(first)
    for i, w in enumerate(S):
        for j, z in enumerate(S):
            if j >= i:
                break
            cnt = 0
            for l in range(L):
                if w[l] != z[l]:
                    cnt += 1
            if cnt <= 1:
                E[i].append(j)
                E[j].append(i)
    d = deque([start])
    V = [-1 for _ in range(N+2)]
    V[start] = 0
    root = [-1]*(N+2)
    while d:
        v = d.popleft()
        t = V[v]
        for w in E[v]:
            if V[w] == -1:
                V[w] = t+1
                d.append(w)
                root[w] = v
                if w == goal:
                    d = []
                    break
    ANS = []
    g = goal
    if root[g] == -1:
        print(-1)
        return
    while g != -1:
        ANS.append(S[g])
        g = root[g]
    print( len(ANS)-2)
    print( "\n".join( ANS[::-1]))
    
if __name__ == '__main__':
    main()
