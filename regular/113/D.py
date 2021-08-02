#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N, M, K = map(int,input().split())
    ans = 0
    if N == 1 or M == 1:
        print(pow(K,max(N,M),Q))
        return
    for k in range(1,K+1):
        ans +=  (pow(k,N,Q) - pow(k-1,N,Q))%Q*pow(K-k+1,M,Q)%Q
        # print((pow(k,N,Q) - pow(k-1,N,Q))%Q,pow(K-k+1,M,Q)%Q)
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
