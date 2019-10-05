#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N = int( input())
    X = list( map( int, list( input())))[::-1]
    c = 0
    for i in range(N):
        c += X[i]*pow(2, i, Q)

    if N%2 == 0:
        print(N*2%Q*c%Q)
        return
if __name__ == '__main__':
    main()
