import sys
from bisect import bisect_left
input = sys.stdin.readline
Q = 998244353
def main():
    N = int( input())
    X = [0]*N
    Y = [0]*N
    XY = [ tuple( map( int, input().split())) for _ in range(N)]
    for i in range(N):
        X[i], Y[i] = XY[i]
    X.sort()
    Y.sort()
    ans = pow(2, N, Q)*N%Q
    s = pow(2, Q-2, Q)
    for x, y in XY:
        i = bisect_left(X,x)
        j = bisect_left(Y,y)
        now = 0
        if i > 1:
            now = ( now + pow(2,i,Q)-1-i)%Q
        if i < N-1:
            now = ( now + pow(2,N-i,Q)-1-(N-i))
        if j > 1:
            now = ( now + pow(2,j,Q)-1-j)%Q
        if j < N-1:
            now = ( now + pow(2,N-j,Q)-1-(N-j))
        ans = ( ans - now*s%Q)%Q
    print( ans)

if __name__ == '__main__':
    main()
 
