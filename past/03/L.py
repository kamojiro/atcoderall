#import sys
#input = sys.stdin.readline
from collections import deque
import heapq
def main():
    N = int( input())
    KT = [ list( map( int, input().split())) for _ in range(N)]
    M = int( input())
    A = list( map( int, input().split()))
    S1 = [2]*N
    S2 = [2]*N
    h1 = []
    h2 = []
    for i in range(N):
        heapq.heappush(h1, (-KT[i][1], i, 1))
        heapq.heappush(h2, (-KT[i][1], i, 1))
        if KT[i][0] >= 2:
            heapq.heappush(h2, (-KT[i][2], i, 2))
            S2[i] += 1
    ANS = []
    for a in A:
        if a == 1:
            while True:
                if KT[h1[0][1]][h1[0][2]] > 0:
                    break
                heapq.heappop(h1)
            ans, i, j = heapq.heappop(h1)
            ANS.append(-ans)
            KT[i][j] = 0
            if KT[i][0] >= S1[i]:
                heapq.heappush(h1, (-KT[i][S1[i]], i, S1[i]))
                S1[i] += 1
            if KT[i][0] >= S2[i]:
                heapq.heappush(h2, (-KT[i][S1[i]], i, S2[i]))
                S2[i] += 1
        else:
            while True:
                if KT[h2[0][1]][h2[0][2]] > 0:
                    break
                heapq.heappop(h2)
            ans, i, j = heapq.heappop(h2)
            ANS.append(-ans)
            KT[i][j] = 0
            if KT[i][0] >= S1[i]:
                heapq.heappush(h1, (-KT[i][S1[i]], i, S1[i]))
                S1[i] += 1
            if KT[i][0] >= S2[i]:
                heapq.heappush(h2, (-KT[i][S1[i]], i, S2[i]))
                S2[i] += 1
    print("\n".join( map( str, ANS)))
    
if __name__ == '__main__':
    main()
