#import sys
#input = sys.stdin.readline
from collections import defaultdict, deque
def main():
    N, M = map( int, input().split())
    X = list( map( int, input().split()))
    Y = [deque() for _ in range(M)]
    Need = [0]*M
    d = defaultdict( int)
    e = defaultdict( int)
    for x in X:
        Y[x%M].append(x)
        if d[(-x)%M] > 0:
            Need[x%M] += 1
            Need[(-x)%M] += 1
            d[(-x)%M] -= 1
        d[x%M] += 1
        e[x] += 1
    set???
    
    
    
if __name__ == '__main__':
    main()
