#import sys
#input = sys.stdin.readline
def main():
    N, L = map( int, input().split())
    S = [ input() for _ in range(N)]
    S.sort()
    V = [1]*N
    print("".join(S))

if __name__ == '__main__':
    main()
