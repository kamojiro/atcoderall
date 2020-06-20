import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify
def main():
    N, Q = map( int, input().split())
    AB = [ tuple( map( int, input().split())) for _ in range(N)]
    CD = [ tuple( map( int, input().split())) for _ in range(Q)]
    HQ = [[] for _ in range(2*10**5+1)]
    Y = [0]
    i = 1
    for a, b in AB:
        heappush(HQ[b], (-a,i))
        Y.append(b)
        i += 1
    ANS = []
    M = []
    for hq in HQ:
        if hq:
            a, i = hq[0]
            M.append((-a,i,Y[i]))
    heapify(M)
    # print(M)
    for c, d in CD:
        y = Y[c]
        Y[c] = d
        t = (-1,-1)
        if HQ[y]:
            t = HQ[y][0]
        while HQ[y]:
            _, i = HQ[y][0]
            if Y[i] == y:
                break
            heappop(HQ[y])
        if HQ[y]:
            if t != HQ[y][0]:
                g, i = HQ[y][0]
                heappush(M, (-g,i,y))
        heappush(HQ[d], (-AB[c-1][0], c))
        a, i = HQ[d][0]
        heappush(M, (-a,i, d ))
        while HQ[d]:
            _, i = HQ[d][0]
            if Y[i] == d:
                break
            heappop(HQ[d])
        while M:
            m,i, z = M[0]
            if Y[i] == z:
                # print( z, HQ[z], M[0])
                g, j = HQ[z][0]
                if i == j:
                    ANS.append(m)
                    break
            heappop(M)
        # print(M)
    print("\n".join( map( str, ANS)))

        
        
if __name__ == '__main__':
    main()
