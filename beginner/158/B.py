#import sys
#input = sys.stdin.readline
def main():
    N, A, B = map( int, input().split())
    n = N//(A+B)
    ans = n*A
    N -= n*(A+B)
    if N <= A:
        ans += N
    else:
        ans += A
    print(ans )
if __name__ == '__main__':
    main()
