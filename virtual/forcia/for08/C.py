#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    XY = [ tuple( map( int, input().split())) for _ in range(N)]
    if N <= 3:
        print(0)
        return
    
if __name__ == '__main__':
    main()
