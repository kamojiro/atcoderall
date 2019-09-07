import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    A = [ deque( map( int, input().split())) for _ in range(N)]
    cnt = N*(N-1)
    days = 0
    W = [False]*N
    while cnt > 0:
        days += 1
        now = cnt
        V = [0]*N
        for i in range(N):
            if V[i] == 1 or W[i]:
                continue
            a = A[i][0]
            a -= 1
            if V[a] == 1 or W[a]:
                continue
            if i+1 == A[a][0]:
                V[a] = 1
                V[i] = 1
                A[a].popleft()
                A[i].popleft()
                if not A[a]:
                    W[a] = True
                if not A[i]:
                    W[i] = True
                cnt -= 2
        if now == cnt:
            print(-1)
            return
    print( days)

                        
if __name__ == '__main__':
    main()
