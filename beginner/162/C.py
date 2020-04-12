#import sys
#input = sys.stdin.readline
from math import gcd
def main():
    K = int( input())
    ans = 0
    GCD = [0]*201
    for i in range(1,K+1):
        for j in range(1, K+1):
            GCD[gcd(i,j)] += 1
    for i in range(1, K+1):
        for k in range(1, K+1):
            ans += gcd(i, k)*GCD[i]
    print(ans)
if __name__ == '__main__':
    main()
