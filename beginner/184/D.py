#import sys
#input = sys.stdin.readline

def main():
    A, B, C = map( int, input().split())
    dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
    dprob = [[[0]*101 for _ in range(101)] for _ in range(101)]
    dprob[A][B][C] = 1
    for i in range(A,100):
        for j in range(B,100):
            for k in range(C,100):
                t = dp[i][j][k]
                s = dprob[i][j][k]
                if A > 0:
                    dp[i+1][j][k] += (t+s)*i/(i+j+k)
                    dprob[i+1][j][k] += s*i/(i+j+k)
                if B > 0:
                    dp[i][j+1][k] += (t+s)*j/(i+j+k)
                    dprob[i][j+1][k] += s*j/(i+j+k)
                if C > 0:
                    dp[i][j][k+1] += (t+s)*k/(i+j+k)
                    dprob[i][j][k+1] += s*k/(i+j+k)
    ans = 0
    for j in range(B,100):
        for k in range(C,100):
            ans += dp[100][j][k]
    for i in range(A,100):
        for k in range(C,100):
            ans += dp[i][100][k]
    for i in range(A,100):
        for j in range(B,100):
            ans += dp[i][j][100]
    print(ans)
if __name__ == '__main__':
    main()
