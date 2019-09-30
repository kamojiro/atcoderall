#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = [ (A[i], i+1) for i in range(N)]
    B.sort()
    print( " ".join( map( str, map( lambda x:x[1], B))))
if __name__ == '__main__':
    main()
