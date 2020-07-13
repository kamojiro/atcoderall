#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    D = [ int( input()) for _ in range(N)]
    S = sum(D)
    M = max(D)
    print(S)
    print( max(0, M - (S-M)))
if __name__ == '__main__':
    main()

