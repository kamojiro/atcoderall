#import sys
#input = sys.stdin.readline
def main():
    A, B, N = map( int, input().split())
    for i in range(N+1):
        print("x=", i, A*i//B-i//B*A)
if __name__ == '__main__':
    main()
