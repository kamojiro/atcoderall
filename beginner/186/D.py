#import sys
#input = sys.stdin.readline
from bisect import bisect_left
from itertools import accumulate
def main():
    N = int( input())
    A = list( map( int, input().split()))
    A.sort()
    accA = list(accumulate([0]+A))
    ans = 0
    for a in A:
        i = bisect_left(A,a)
        ans += a*i - accA[i]
        ans += (accA[-1] - accA[i]) - a*(N-i)

    print(ans//2)
if __name__ == '__main__':
    main()
