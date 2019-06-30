Q = 10**9+7
from collections import deque
from itertools import accumulate
#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    ans = 0
    d = deque()
    e = deque()
    M = int(N**(1/2))*2
    for i in range(1, int(N**(1/2))+1):
        if i**2 == N:
            d.append(i)
            M -= 1
            continue
        d.append(i)
        e.appendleft(N//i)
    T = list(d)+list(e)
    CT = [1]*M
    for i in range(1,M):
        CT[i] = T[i] - T[i-1]
    accT = list( map(lambda x:x%Q, accumulate(CT) ))
    dp = [[0]*M for _ in range(K)]
    for i in range(M):
        dp[1][i] = accT[-i-1]*CT[i]%Q
    for k in range(1, K-1):
        accT[0] = dp[k][0]
        for i in range(M-1):
            accT[i+1] = (accT[i]+dp[k][i+1])%Q
        for i in range(M):
            dp[k+1][i] = accT[-i-1]*CT[i]%Q
    print(sum(dp[K-1])%Q)
    
if __name__ == '__main__':
    main()
