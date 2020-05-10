#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N, M, K = map( int, input().split())
    ans = 0
    cmb = 1
    for k in range(K+1):
        ans += M*pow(M-1,N-1-k,Q)%Q*cmb%Q
        ans %= Q
        cmb *= (N-k-1)*pow(k+1,Q-2,Q)%Q
        cmb %= Q
    print(ans)
if __name__ == '__main__':
    main()
