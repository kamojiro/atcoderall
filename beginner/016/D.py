#import sys
#input = sys.stdin.readline

def area(px, py, qx, qy, rx, ry):
    return (qx-px)*(ry-py) - (rx-px)*(qy-py)

def main():
    ax, ay, bx, by = map( int, input().split())
    N = int( input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map( int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        j = (i+1)%N
        if area(ax,ay,bx,by,X[i],Y[i])*area(ax,ay,bx,by,X[j],Y[j]) < 0 and area(X[i],Y[i],X[j],Y[j],ax,ay)*area(X[i],Y[i],X[j],Y[j],bx,by) < 0:
            ans += 1
    ans //= 2
    print( ans+1)
if __name__ == '__main__':
    main()
