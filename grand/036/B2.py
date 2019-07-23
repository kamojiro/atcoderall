#import sys
#input = sys.stdin.readline
from collections import defaultdict, deque
from math import log2
def main():
    n, k = map( int, input().split())
    A = list( map( int, input().split()))
    logNK = int(log2(n) + log2(k))
    double = [ [0]*(logNK+1) for _ in range(n)]
    d = defaultdict( lambda :-1)
    for i in range(n):
        if d[A[i]] == -1:
            d[A[i]] = i
            continue
        double[d[A[i]]][0] = (i+1)%N
        d[A[i]] = i
    for i in range(n):
        if d[A[i]] > -1:
            double[d[A[i]]][0] = (i+1)%N
            d[A[i]] = -1
    for i in range(logNK):
        for j in range(N):
            double[j][i+1] = double[double[j][i]][i]
    L = N*K
    now = 0
    for i in range(logNK, -1, -1):
        if pow(2,i) < 
        L -= pow(2, i)
        now
if __name__ == '__main__':
    main()
