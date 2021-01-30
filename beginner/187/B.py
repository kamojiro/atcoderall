#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    XY = [ tuple( map(int,input().split())) for _ in range(N)]
    ans = 0
    for i, z in enumerate(XY[:-1]):
        x1, y1 = z
        for x2, y2 in XY[i+1:]:
            if x1 == x2:
                continue
            # print(x1,y1,x2,y2)
            if -abs(x2-x1) <= (y1-y2)  <= abs(x1-x2):
                # print("N")
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()
