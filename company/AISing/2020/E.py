import sys
input = sys.stdin.readline
def solve():
    N = int( input())
    L = [0]*N
    R = [0]*N
    K = [0]*N
    for i in range(N):
        k, L[i], R[i] = map( int, input().split())
        K[i] = k-1
    


def main():
    T = int( input())
    ANS = [ solve() for _ in range(T)]
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
