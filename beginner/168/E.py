import sys
input = sys.stdin.readline

Q = 10**9+7

from collections import defaultdict
from math import gcd
def main():
    N = int( input())
    AB = [ tuple( map( int, input().split())) for _ in range(N)]
    d = defaultdict( int)
    for a, b in AB:
        if a == 0 and b == 0:
            d[(0,0)] += 1
            continue
        if a == 0:
            d[(0,1)] += 1
            continue
        if b == 0:
            d[(1,0)] += 1
            continue

        g = gcd(a, b)
        a //= g
        b //= g
        if a < 0:
            a = -a
            b = -b
        d[(a,b)] += 1
    # print(d)
    ans = 1
    K = list( d.keys())
    for k in K:
        # print(ans)
        # print("|",k)
        a, b = k
        if a == 0 and b == 0:
            continue
        if a*b == 0:
            ans *= (pow(2,d[(1,0)],Q) + pow(2,d[(0,1)],Q) -1)%Q
            ans %= Q
            d[(1,0)] = 0
            d[(0,1)] = 0
            continue
        if b > 0 and d[(a,b)] > 0 and d[(b,-a)] > 0:
            ans *= (pow(2,d[(a,b)],Q) + pow(2,d[(b,-a)],Q) - 1)%Q
            ans %= Q
            continue
        if b < 0 and d[(a,b)] > 0 and d[(-b,a)] > 0:
            continue
        ans *= pow(2,d[(a,b)],Q)
        ans %= Q
    
    ans -= 1
    ans += d[(0,0)]
    ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
