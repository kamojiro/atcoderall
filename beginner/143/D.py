import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import accumulate
def main():
    N = int( input())
    L = list( map( int, input().split()))
    d = defaultdict( int)
    ans = 0
    
    for l in L:
        d[l] += 1
    L.sort()
    R = list( set(L))
    R.sort()
    for e in d:
        if d[e] >= 3:
            ans += d[e]*(d[e]-1)*(d[e]-2)//6
        if d[e] >= 2:
            cnt = 0
            t = d[e]*(d[e]-1)//2
            for l in R:
                if l == e:
                    continue
                if l < 2*e:
                    cnt += t*d[l]

            ans += cnt
    T = [0]*(10**4)
    M = len(R)
    Z = [0]*(10**4)

    for i in range(M):
        for j in range(i+1, M):
            e = R[i]
            f = R[j]
            t = d[e]*d[f]
            T[ abs(e-f)+1] += t
            T[ e+f] -= t
            if abs(e-f) < e:
                Z[e] += t
            if abs(e-f) < f:
                Z[f] += t
    S = list( accumulate(T))
    a = 0

    for e in d:
        if S[e] > 0:
            a += (S[e] - Z[e])*d[e]

    print(ans+a//3)
if __name__ == '__main__':
    main()
