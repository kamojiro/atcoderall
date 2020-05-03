#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    A = list( map( int, input().split()))
    d = defaultdict( int)
    e = defaultdict( int)
    ans = 0
    for i in range(N):
        a = A[i]
        ans += d[a+(i+1)]
        ans += e[a-(i+1)]
        d[(i+1)-a] += 1
        e[-a-(i+1)] += 1
    
    print(ans)
if __name__ == '__main__':
    main()
