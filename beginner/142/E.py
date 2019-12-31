#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, M = map( int, input().split())
    costs = [0]*M
    keys = [0]*M
    for i in range(M):
        costs[i], b = map( int, input().split())
        C = list( map( int, input().split()))
        key = 0
        for c in C:
            key += pow(2, c-1)
        keys[i] = key
    K = pow(2,N)
    dp =[10**7]*K
    dp[0] = 0
    for i in range(M):
        key = keys[i]
        cost = costs[i]
        for j in range(K):
            if j != (j | key):
                if dp[j] + cost < dp[j|key]:
                    dp[j|key] = dp[j] + cost
    if dp[K-1] == 10**7:
        print(-1)
    else:
        print(dp[K-1])
if __name__ == '__main__':
    main()
