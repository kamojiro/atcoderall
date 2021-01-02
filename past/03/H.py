#import sys
#input = sys.stdin.readline
def main():
    N, L = map( int, input().split())
    X = list( map( int, input().split()))
    T = list( map( int, input().split()))
    H = [False]*(L+1)
    for x in X:
        H[x] = True
    action_one = T[0]
    action_two = T[0]+T[1]
    action_three = T[0]+T[1]*3
    dp = [10**9]*(L+1)
    dp[0] = 0
    t = 0
    for i in range(1,L+1):
        if H[i]:
            t = T[2]
        else:
            t = 0
        if i >= 1:
            if dp[i-1] + action_one + t < dp[i]:
                dp[i] = dp[i-1] + action_one + t
        if i >= 2:
            if dp[i-2] + action_two + t < dp[i]:
                dp[i] = dp[i-2] + action_two + t
        if i >= 4:
            if dp[i-4] + action_three + t < dp[i]:
                dp[i] = dp[i-4] + action_three + t
    ans = dp[L]
    for i in range(1,4):
        if dp[L-i] + T[0]//2 + T[1]//2*(2*i-1) < ans:
            ans = dp[L-i] + T[0]//2 + T[1]//2*(2*i-1)
    print(ans)
    
if __name__ == '__main__':
    main()
