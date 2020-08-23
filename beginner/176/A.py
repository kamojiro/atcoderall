#import sys
#input = sys.stdin.readline
def main():
    N, X, T = map( int, input().split())
    print((N+(X-1))//X*T)
if __name__ == '__main__':
    main()
