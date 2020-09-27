import sys
input = sys.stdin.readline
def main():
    N = int( input())
    U = []
    V = []
    for _ in range(N):
        x, y = map( int, input().split())
        u, v = x+y, x-y
        U.append(u)
        V.append(v)
    U.sort()
    V.sort()
    print( max(U[-1]-U[0], V[-1]-V[0]))
if __name__ == '__main__':
    main()
