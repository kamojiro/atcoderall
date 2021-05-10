#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, K = map(int,input().split())
    dp = [0]*(3*N+1)
    for p in product(range(1,N+1), repeat=3):
        dp[sum(p)] += 1
    print(dp)
    
if __name__ == '__main__':
    main()




