#import sys
#input = sys.stdin.readline
import numpy as np
def main():
    N = int( input())
    P = list( map( int, input().split()))
    N = 100**2+1
    dp = np.zeros(N)
    dp[0] = 1
    for p in P:
        dp[p:] += dp[:N-p]
    # print(dp[:11])
    ans = sum([1 if t > 0 else 0 for t in dp])
    print(ans)
    
if __name__ == '__main__':
    main()
