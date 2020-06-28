Q = 998244353
#import sys
#input = sys.stdin.readline
def main():
    A, B, C, D = map( int, input().split())
    dp = [[0]*3001 for _ in range(3001)]
    dp[A][B] = 1
    N = 3001
    for j in range(B,N-1):
        dp[A][j+1] = dp[A][j]*A%Q
    for i in range(A+1,N):
        for j in range(N):
            
    print([k[:D+1] for k in dp[:C+1]])
    print(dp[C][D])
if __name__ == '__main__':
    main()
