#import sys
#input = sys.stdin.readline
from collections import Counter, defaultdict
Q = 10**9+7
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    CA = Counter(A)
    CB = Counter(B)
    for a in A:
        if CA[a] >= 2:
            print(0)
            return
    for b in B:
        if CB[b] >= 2:
            print(0)
            return
    R = defaultdict( lambda: -1)
    C = defaultdict( lambda: -1)
    for i,a in enumerate(A):
        R[a] = i
    for j, b in enumerate(B):
        C[b] = j
    columns = 0
    rows = 0
    ditermined = 0
    ans = 1
    for n in range(N*M,0,-1):
        if R[n] >= 0 and C[n] >= 0:
            columns += 1
            rows += 1
            ditermined += 1
            continue
        if R[n] >= 0:
            rows += 1
            ans *= columns
            ans %= Q
            ditermined += 1
            continue
        if C[n] >= 0:
            columns += 1
            ans *= rows
            ans %= Q
            ditermined += 1
            continue
        if columns*rows == ditermined:
            print(0)
            return
        ans *= (columns*rows-ditermined)
        ans %= Q
        ditermined += 1
    print(ans)
if __name__ == '__main__':
    main()
