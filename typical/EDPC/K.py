#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    dp = [[None]*2 for _ in range(K+1)]
    for i in range(A[0]):
        dp[i][0] = False
        dp[i][1] = True
    for k in range(A[0], K+1):
        win = False
        for a in A:
            if a <= k:
                if dp[k-a][1]:
                    win = True
                    break
        dp[k][0] = win
        win = True
        for a in A:
            if a <= k:
                if not dp[k-a][0]:
                    win = False
                    break
        dp[k][1] = win
    if dp[K][0]:
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    main()
