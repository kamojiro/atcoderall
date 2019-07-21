#import sys
#input = sys.stdin.readline
def main():
    n, d = map( int, input().split())
    print( (n+d*2)//(d*2+1))
if __name__ == '__main__':
    main()
