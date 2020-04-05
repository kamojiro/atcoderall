#import sys
#input = sys.stdin.readline
def main():
    S, L, R = map( int, input().split())
    if not L <= (ans := S) <= R:
        ans = L if S < L else R
    print(ans)
if __name__ == '__main__':
    main()
