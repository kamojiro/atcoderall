#import sys
#input = sys.stdin.readline
def main():
    N, Ma, Mb = map(int, input().split())
    A = []
    B = []
    C = []
    for _ in range(N):
        a, b, c = map( int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    dp = [[10**5]*401 for _ in range(401)]
    dp[0][0] = 0
    for t in range(N):
        a, b, c = A[t], B[t], C[t]
        for i in range(400,-1,-1):
            for j in range(400,-1,-1):
                if i-a >= 0 and j-b >= 0:
                    if dp[i-a][j-b] + c < dp[i][j]:
                        dp[i][j] = dp[i-a][j-b] + c
    ans = 10**5
    for i in range(1, 401):
        if i*Ma > 400 or i*Mb > 400:
            break
        if dp[i*Ma][i*Mb] < ans:
            ans = dp[i*Ma][i*Mb]
    if ans == 10**5:
        print(-1)
    else:
        print(ans)
    
if __name__ == '__main__':
    main()
