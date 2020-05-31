#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N, S = map( int, input().split())
    A = list( map( int, input().split()))
    invtwo = pow(2, Q-2, Q)
    # Invtwo = [1]
    # now = 1
    dp = [pow(2, N, Q)]+[0]*S
    for i in range(N):
        a = A[i]
        for i in range(S, a-1,-1):
            # print(i, a, i-a, dp[i-a])
            if dp[i-a] > 0:
                dp[i] += dp[i-a]*invtwo%Q
                dp[i] %= Q
        # print(dp)
    print(dp[S])
                
if __name__ == '__main__':
    main()
