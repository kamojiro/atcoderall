#import sys
#input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations
def main():
    N, M, P, Q, R = map( int, input().split())
    d = defaultdict( int)
    for _ in range(R):
        x, y, z = map( int, input().split())
        d[(x-1,y-1)] = z
    ans = 0
    for pcomb in combinations(range(N), P):
        G = [0]*M
        for m in range(M):
            for w in pcomb:
                G[m] += d[(w,m)]
        G.sort(reverse=True)
        ret = sum( G[:Q])
        
        if ans < ret:
            ans = ret
    print(ans)
if __name__ == '__main__':
    main()
