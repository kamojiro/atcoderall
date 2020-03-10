#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    ans = (K-1)*(N-K)*6 + (N-K)*3 + (K-1)*3 + 1
    print(ans/(N**3))
if __name__ == '__main__':
    main()
