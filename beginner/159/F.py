#import sys
#input = sys.stdin.readline
Q = 998244353
def cmb(n,r):
    if n-r < r: r = n-r
    if r == 0: return 1
    denominator = 1                       #分母
    numerator = 1                         #分子
    for i in range(r):
        numerator *= n-i
        numerator %= Q
        denominator *= i+1
        denominator %= Q
    return numerator*pow(denominator, Q-2, Q)%Q

def main():
    N, S = map( int, input().split())
    A = list( map( int, input().split()))
    dp = [ [0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a = A[i]
        g = (i+1)*(N-i)%Q
        for j in range(a,S+1):
            dp[i+1][j] = dp[i][j-a]*g
    ans = 0
    print(dp)
    for i in range(N+1):
        ans += dp[N][i]*i
        ans %= Q
    print(ans)
        
        
if __name__ == '__main__':
    main()
