#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    A.sort()
    print( sum(A[N::2]))
if __name__ == '__main__':
    main()
