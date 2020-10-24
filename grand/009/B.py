import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int(input())
    A = [int(input()) for _ in range(N-1)]
    E = [[] for _ in range(N)]
    for i, a in enumerate(A):
        E[a-1].append(i+1)
    d = deque([0])
    Z = [0]
    V = [False]*N
    V[0] = True
    while d:
        v = d.popleft()
        for w in E[v]:
            if not V[w]:
                V[w] = True
                Z.append(w)
                d.append(w)
    D = [[] for _ in range(N)]
    T = [0]*N
    for z in Z[::-1]:
        count = 1
        P = []
        for v in E[z]:
            P.append(T[v])
        P.sort(reverse=True)
        for i, p in enumerate(P):
            if count < p+i+1:
                count = p+i+1
        T[z] = count
    print(T[0]-1)
    
if __name__ == '__main__':
    main()
