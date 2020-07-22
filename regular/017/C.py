#import sys
#input = sys.stdin.readline
from itertools import product
from collections import defaultdict
def main():
    N, X = map( int, input().split())
    W = [ int( input()) for _ in range(N)]
    d = defaultdict( int)
    m, n = N//2, N-N//2
    for p in product(range(2), repeat=m):
        weight = 0
        for i in range(m):
            if p[i] == 1:
                weight += W[i]
        d[weight] += 1
    ans = 0
    # print(d)
    for p in product(range(2), repeat=n):
        weight = 0
        for i in range(n):
            if p[i] == 1:
                weight += W[i+m]
        if weight <= X:
            ans += d[X-weight]
    print(ans)
            
if __name__ == '__main__':
    main()
