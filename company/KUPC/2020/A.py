#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    XY = [tuple(map(int,input().split())) for _ in range(N)]
    ans = 0
    px, py = XY[0]
    for x, y in XY[1:]:
        ans += abs(x-px)+abs(y-py)
        px, py = x, y
    print(ans)
if __name__ == '__main__':
    main()
