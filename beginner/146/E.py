#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()));
    M = [0]*N
    d = defaultdict( int)
    d[0] = 1
    now = 0
    ans = 0
    if K == 1:
        print(sum( list( map(lambda x: x%2, A))))
        return
    for i in range(N):

    # if A[i]%K == 1:
    #         ans += 1
#            print(i-(K-1), M[i-(K-1)], d)
        now = (now + A[i] - 1)%K
        M[i] = now
        ans += d[now]
        if i == K-2:
            d[0] -= 1

        if i >= K-1:
            d[M[i-(K-1)]] -= 1

        d[now] += 1
        #print(ans)        
        # print(i, ans)

    print(ans)
        
if __name__ == '__main__':
    main()


