#import sys
#input = sys.stdin.readline
from heapq import heappush, heappop
def main():
    H, W = map( int, input().split())
    C = [ list( map( int, input().split())) for _ in range(10)]
    A = [ list( map( int, input().split())) for _ in range(H)]
    h = [(0,1)]
    V = [-1]*10
    while h:
        # print(h)
        m, n = heappop(h)
        if V[n] > -1:
            continue
        V[n] = m
        for i in range(10):
            if V[i] == -1:
                heappush(h, (m+C[i][n],i))
    # print(V)
    ans = 0
    for a in A:
        for b in a:
            if b > -1:
                ans += V[b]
    print(ans)
    
if __name__ == '__main__':
    main()
