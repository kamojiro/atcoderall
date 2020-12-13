#import sys
#input = sys.stdin.readline
from copy import deepcopy
def solve(N,Q):
    Z = [0]*(N+1)
    P = deepcopy(Q)
    for i, p in enumerate(P):
        Z[p] = i
    permuted = [False]*N
    for n in range(1,N+1):
        if Z[n] == n-1:
            continue
        K = Z[n]
        for i in range(K-1,n-2,-1):
            if permuted[i]:
                return False
                return
            Z[P[i+1]] = i
            Z[P[i]] = i+1
            P[i], P[i+1] = P[i+1], P[i]
            permuted[i] = True
    return P
        
from itertools import permutations

            
def main():
    N = int( input())
    for p in permutations(range(1,N+1)):
        Q = list(p)
        print(Q, end=" ")
        print(solve(N,Q))
    # print(solve(4,[1,4,2,3]))
if __name__ == '__main__':
    main()
