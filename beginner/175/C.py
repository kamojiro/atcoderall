#import sys
#input = sys.stdin.readline
def main():
    X, K, D = map( int, input().split())
    if X < 0:
        X = -X
    c = min(X//D, K)
    X -= c*D
    K -= c
    if K%2 == 0:
        print(X)
    else:
        print(D-X)
    
if __name__ == '__main__':
    main()
