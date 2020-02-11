#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    N, S, T = map( int, input().split())
    A = list( accumulate([ int( input()) for _ in range(N)]))
    ans = 0
    for a in A:
        if S <= a <= T:
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()
