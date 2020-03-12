#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    A = list( map( int, input().split()))
    A.sort()
    d = defaultdict( lambda: False)
    M = 10**9
    ans = 0
    for a in A:
        if d[a]:
            continue
        ans += 1
        while a <= M:
            d[a] = True
            a *= 2
    print(ans)
    
if __name__ == '__main__':
    main()
