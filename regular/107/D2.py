import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
Q = 998244353
def main():
    N, K = map(int,input().split())
    dp = [[0]*(N+1) for i in range(N+1)]
    checked = [[False]*(N+1) for i in range(N+1)]
    for i in range(N+1):
        for j in range(i):
            dp[i][j] = 0
    for i in range(N+1):
        dp[i][i] = 1
        checked[i][i] = True
    def f(n,k):
        if n == k:
            return 1
        if n < k:
            return 0
        if checked[n][k]:
            return dp[n][k]
        ret = 0
        checked[n][k] = True
        for t in range(k+1):
            if n-(k-t) < t*2:
                break
            ret += f(n-(k-t),t*2)
            ret %= Q
        return ret
    print(f(N,K))
    
if __name__ == '__main__':
    main()
