#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = [0]*(N+1)
    for a in A:
        B[a] += 1
    print("\n".join( map( str, B[1:])))
if __name__ == '__main__':
    main()
