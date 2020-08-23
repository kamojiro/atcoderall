import numpy as np
def main():
    N = int( input())
    P = list( map( int, input().split()))
    N = 100**2+1
    dp = np.full(N, False)
    dp[0] = True
    for p in P:
        dp[p:] |= dp[:N-p]
    # # print(dp[:11])
    # ans = sum([1 if t > 0 else 0 for t in dp])
    print( dp.sum())
    
if __name__ == '__main__':
    main()
