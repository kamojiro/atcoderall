#import sys
#input = sys.stdin.readline
def main():
    H = int( input())
    W = int( input())
    N = int( input())
    if H < W:
        H, W = W, H
    ans = N//H
    if N%H != 0:
        ans += 1
    print(ans)
if __name__ == '__main__':
    main()
