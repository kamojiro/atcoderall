import sys
input = sys.stdin.readline
def main():
    N, K, Q = map( int, input().split())
    A = [ int( input()) for _ in range(Q)]
    Point = [-Q]*N
    for a in A:
        Point[a-1] += 1
    for i in range(N):
        if K + Point[i] <= 0:
            print('No')
        else:
            print('Yes')
if __name__ == '__main__':
    main()
