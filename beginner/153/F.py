import sys
input = sys.stdin.readline
from bisect import bisect_right
def main():
    N, D, A = map( int, input().split())
    XH = []
    X = []
    for _ in range(N):
        x, h = map( int, input().split())
        XH.append( (x, (h+(A-1))//A))
        X.append(x)
    XH.sort()
    X.sort()
    T = [0]*(N+1)
    j = 0
    now = 0
    ans = 0
    for i in range(N):
        x, h = XH[i]
        now -= T[i]
        if now >= h:
            continue
        else:
            T[ bisect_right(X,x+D*2)] += h-now
            ans += h - now
            now = h
    print(ans)
if __name__ == '__main__':
    main()
