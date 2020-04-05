from math import gcd
#import sys
#input = sys.stdin.readline
def main():
    N, Q = map( int, input().split())
    A = list( map( int, input().split()))
    S = list( map( int, input().split()))
    a = A[0]
    G = []
    for b in A:
        a = gcd(a, b)
        G.append(a)
    for s in S:
        # if ( ans := gcd(s, a)) > 1:
        #     print( ans)
        #     continue

        if gcd(s, a) > 1:
            print( gcd(s,a))
            continue
        l = -1
        r = N
        while r - l > 1:
            m = (l+r)//2
            if gcd(s, G[m]) == 1:
                r = m
            else:
                l = m
        print(r+1)
if __name__ == '__main__':
    main()
