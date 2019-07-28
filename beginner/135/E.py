#import sys
#input = sys.stdin.readline
def main():
    K = int( input())
    X, Y = map( int, input().split())
    if K%2 == 0:
        if (X+Y)%2 == 1:
            print(-1)
            return
    abX = abs(X)
    abY = abs(Y)
    a, b = 1, 1
    if X < 0:
        a = -1
    if Y < 0:
        b = -1
    if (X+Y)%K == 0:
        print(abX//K+abY//K+1)
    elif (X-Y)%K == 0:
        print(abX//K+abY//K+2)
    else:
        print(abX//K+abY//K+3)
    x, y = 0, 0
    for _ in range(abX//K):
        x += a*K
        print(x,y)
    for _ in range(abY//K):
        y += b*K
        print(x,y)
    if (X+Y)%K == 0:
        print(X,Y)
        return
    if (X-Y)%K == 0:
        print(x+a*K, y)
        print(X,Y)
        return
    
    print(X,y)
    print(X,Y)
if __name__ == '__main__':
    main()
