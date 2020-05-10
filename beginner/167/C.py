#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, M, X = map( int, input().split())
    A = [ list( map( int, input().split())) for _ in range(N)]

    Alg = [0]*M
    cost = 0
    for a in A:
        cost += a[0]
        for i in range(M):
            Alg[i] += a[i+1]
    for i in range(M):
        if Alg[i] < X:
            print(-1)
            return

    ans = cost
    for P in product( range(2), repeat=N):
        Alg = [0]*M
        cost = 0
        for i in range(N):
            if P[i] == 0:
                continue
            cost += A[i][0]
            for j in range(M):
                Alg[j] += A[i][j+1]
        check = True
        for i in range(M):
            if Alg[i] < X:
                check = False
                break
        if check:
            if cost < ans:
                ans = cost
    print(ans)
        
if __name__ == '__main__':
    main()
