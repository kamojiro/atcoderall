#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    A = sum( list( map( int, input().split())))
    if N < A:
        print(-1)
    else:
        print(N-A)
if __name__ == '__main__':
    main()
