#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    N = int( input())
    ans = pow(10, N, Q) - pow(9, N, Q)*2 + pow(8, N, Q)
    print( ans%Q)
if __name__ == '__main__':
    main()
