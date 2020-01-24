#import sys
#input = sys.stdin.readline
def main():
    N, K, S = map( int, input().split())
    t = 1
    if S <= N:
        t = N+1
    ANS = [S]*K + [t]*(N-K)
    print(" ".join( map( str, ANS)))
if __name__ == '__main__':
    main()
