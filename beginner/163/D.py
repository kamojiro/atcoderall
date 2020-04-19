#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    N, K = map( int, input().split())
    m = 0
    M = 0
    for i in range(K-1):
        m += i
        M += N-i
    ans = 0
    for i in range(K-1, N+1):
        m += i
        M += N-i

        ans += M-m+1
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
