#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    for i in range(K):
        B = [0]*(N+1)
        for j in range(N):
            d = A[j]
            x = j-d
            y = j+d
            if x < 0:
                B[0] += 1
            else:
                B[x] += 1
            if N-1 < y:
                B[N] -= 1
            else:
                B[y+1] -= 1
        A = list( accumulate(B))
        check = True
        for j in range(N):
            if A[j] < N:
                check = False
        if check:
            break
    print(" ".join( map(str, A[:-1])))
            
if __name__ == '__main__':
    main()
