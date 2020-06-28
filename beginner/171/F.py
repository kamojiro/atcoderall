#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    K = int( input())
    S = input()
    N = len(S)
    if N == 1:
        print((pow(26,K+1,Q) - pow(25,K+1,Q))%Q)
        return
    n = K+N+1
    ans = (pow(26,n,Q) - pow(25,n,Q))%Q
    print(ans)
    t = 0
    for i in range(1, n+1):
        t += pow(i,N-3,Q)
        t %= Q
    ans = (ans - t*pow(25,n,Q)%Q)%Q
    print(ans)
if __name__ == '__main__':
    main()
