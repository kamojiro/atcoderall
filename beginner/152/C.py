#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    P = list( map( int, input().split()))
    ans = 0
    now = P[0]
    for p in P:
        if now >= p:
            ans += 1
            now = p
    print(ans)
if __name__ == '__main__':
    main()
