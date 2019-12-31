import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def main():
    N = int( input())
    A = list( map( int, input().split()))
    dp = [[-1]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][i] = 0

    def rec(l, r, N, A):
        if dp[l][r] >= 0:
            return dp[l][r]
        if (N-(r-l))%2 == 1:
            if rec(l+1,r,N,A) < rec(l, r-1,N,A):
                dp[l][r] = rec(l+1,r,N,A)
            else:
                dp[l][r] = rec(l, r-1,N,A)
        else:
            if rec(l+1, r,N,A)+A[l] > rec(l,r-1,N,A)+A[r-1]:
                dp[l][r] = rec(l+1, r,N,A)+A[l]
            else:
                dp[l][r] = rec(l,r-1,N,A)+A[r-1]
#        print(l, r,dp[l][r], dp)
        return dp[l][r]
    print(2*rec(0, N, N, A) - sum(A))
#    print(dp)
if __name__ == '__main__':
    main()
