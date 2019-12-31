#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int ,input().split())
    A = list( map(int, input().split()))
    dp = [False]*(K+1)
    for i in range(A[0],K+1):
        for a in A:
            if a > i:
                break
            dp[i] |= not dp[i-a]
    if dp[K]:
        print("First")
    else:
        print("Second")
if __name__ == '__main__':
    main()
