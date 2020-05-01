#import sys
#input = sys.stdin.readline
def main():
    N, A, B = map( int, input().split())
    if (B-A)%2 == 0:
        print((B-A)//2)
    else:
        print( min( A+(B-A-1)//2, N+1-B+(B-A-1)//2))
if __name__ == '__main__':
    main()
