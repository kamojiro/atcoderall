#import sys
#input = sys.stdin.readline
from heapq import heappush, heappop
from numba import njit, b1, i4, i8, f8

def main():
    N = int(input())
    XYZ = [ tuple(map(int,input().split())) for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    for i, abc in enumerate(XYZ):
        a, b, c = abc
        for j, pqr in enumerate(XYZ):
            if i == j:
                continue
            p, q, r = pqr
            dist[i][j] = abs(p-a) + abs(q-b) + max(0,r-c)
    pow2 = [1]
    for _ in range(N-1):
        pow2.append(pow2[-1]*2)
    pows = []
    for i, p in enumerate(pow2):
        if i == 0:
            continue
        pows.append((i,p))
        
    INF = 10**10
    # 逆だから気をつける
    # cities = [[INF]*(2**N) for _ in range(N)]
    # determined = [[False]*(2**N) for _ in range(N)]
    f = 2**N
    cities = [INF]*(f*N)
    determined = [False]*(f*N)
    df = dict()
    ind = 0
    # for i in range(N):
    #     for j in range(2**N):
    #         df[ind] = (i,j)
    #         ind += 1
    # q = [(0,0,1)]
    q = [(0,1)]
    cities[1] = 0

    
    while q:
        d, ind = heappop(q)
        v,e = ind//f, ind%f
        if determined[ind]:
            continue
        # cities[v][e] = d
        determined[ind] = True
        for i, p in pows:
            if e&p > 0:
                continue
            # print(e+p)
            if d+dist[v][i] < cities[i*f+e+p]:
                cities[i*f+e+p] = d+dist[v][i]
                heappush(q, (d+dist[v][i], i*f+e+p))
    ANS = []
    # print(dist)
    occ = 2**N-1
    # print(cities)
    for i in range(N):
        ANS.append(cities[i*f+occ]+dist[i][0])
    print(min(ANS))
    # print(cities[0][-1])
        
if __name__ == '__main__':
    main()
