#import sys
#input = sys.stdin.readline
from collections import deque
from bisect import bisect_left

def main():
    N, Q = map( int, input().split())
    Query = [ tuple( map( int, input().split())) for _ in range(Q)]
    LX = 1
    X = deque([N])
    VX = deque([N])
    LY = 1
    Y = deque([N])
    VY = deque([N])
    mx = N
    my = N
    ans = 0
    # ANS = [0]
    for i, x in Query:
        if i == 1:
            if x < my:
                ans += mx-2
                # Y.appendleft(x)
                # VY.appendleft(mx)
                X.appendleft(x)
                VX.appendleft(mx)
                my = x
            else:
                ans += VX[bisect_left(X,x)-1]-2
                # print("x", x, bisect_left(X,x))
                # print(X, VX)
        else:
            if x < mx:
                ans += my-2
                Y.appendleft(x)
                VY.appendleft(my)

                # X.appendleft(x)
                # VX.appendleft(my)
                mx = x
            else:
                ans += VY[bisect_left(Y,x)-1]-2
                # print("y",x, bisect_left(Y,x))
                # print(Y, VY)

        # print(X, VX)
        # print( ans-ANS[-1])
        # ANS.append(ans)
    #     print(i, x, ans)
    # print(X, VX)
    # print(Y,VY)
    print((N-2)**2-ans)
if __name__ == '__main__':
    main()
