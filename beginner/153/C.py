#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    H = list( map( int, input().split()))
    if N <= K:
        print("0")
        return
    H.sort( reverse=True)
    print( sum( H[K:]))
if __name__ == '__main__':
    main()
