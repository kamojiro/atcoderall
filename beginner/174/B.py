#import sys
#input = sys.stdin.readline
def main():
    N, D = map( int, input().split())
    XY = [ tuple( map(int, input().split())) for _ in range(N)]
    ans = 0
    d = D**2
    for x,y in XY:
        if x**2 + y**2 <= d:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()
