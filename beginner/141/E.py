#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = input()
    dp = [[0]*(N+1) for _ in range(N+1)]
    c = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if S[i] == S[j]:
                c = dp[i][j] + 1
                if c > j-i:
                    dp[i+1][j+1] = j-i
                else:
                    dp[i+1][j+1] = c
    for i in range(N+1):
        print(dp[i])
    print( max( [ max(dp[i]) for i in range(N+1)]))
if __name__ == '__main__':
    main()





