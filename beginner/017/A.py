#import sys
#input = sys.stdin.readline
def main():
    ans = 0
    for s, e in [ tuple( map( int, input().split())) for _ in range(3)]:
        ans += s*e//10
    print(ans)
if __name__ == '__main__':
    main()
