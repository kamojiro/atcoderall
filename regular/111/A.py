#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    q = pow(10,N,M**2)
    print(q//M%M)
if __name__ == '__main__':
    main()
