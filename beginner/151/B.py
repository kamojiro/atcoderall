#import sys
#input = sys.stdin.readline
def main():
    N, K, M = map( int, input().split())
    S = sum( list( map( int, input().split())))
    t = N*M - S
    if t <= 0:
        print(0)
    elif t <= K:
        print(t)
    else:
        print(-1)
if __name__ == '__main__':
    main()
