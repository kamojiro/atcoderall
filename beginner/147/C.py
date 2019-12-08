import sys
from itertools import product
#from collections import defaultdict
input = sys.stdin.readline
def main():
    N = int( input())
    A = [[0]*N for _ in range(N)]
    C = [0]*N
    for i in range(N):
        C[i] = int( input())
        for _ in range(C[i]):
            x, y = map( int, input().split())
            A[i][x-1] = -1+y*2
    ans = 0
    T = [-1, 1]
    for P in product( range(-1, 2, 2), repeat = N):
        check = True
        for i in range(N):
            if P[i] == -1:
                continue
            for j in range(N):
                if A[i][j] == 0:
                    continue
                if A[i][j]*P[i] != P[j]:
                    check = False
                    break
        if check:
            if ans < (sum(P) + N)//2:
                ans = (sum(P) + N)//2
    print(ans)
if __name__ == '__main__':
    main()
