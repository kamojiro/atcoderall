import sys
input = sys.stdin.readline
from itertools import permutations, accumulate
from bisect import bisect_right
def main():
    N, M = map(int,input().split())
    W = list(map(int,input().split()))
    L = []
    V = []
    for i in range(M):
        l, v = map(int,input().split())
        L.append((l,i))
        V.append(v)
    minv = min(V)
    maxv = max(V)
    maxw = max(W)
    if minv < maxw:
        print(-1)
        return
    L.sort(lambda x:x[0])
    MV = [0]*M
    MV[-1] = maxv
    for i in range(M-2,-1,-1):
        MV[i] = min(MV[i+1],V[L[i][1]])
    C = [[0]*N for _ in range(N)]
    for p in permutations(W):
        accp = [0] + list(accumulate(p))
        for i in range(N-1):
            for j in range(i+1,N):
                w = accp[j] - accp[i]
                index = bisect_right(MV,w-1)
                
                
                
                
    
    
    
    
if __name__ == '__main__':
    main()
