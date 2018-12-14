from heapq import *
from collections import defaultdict
N = int( input())
A = [ [0]*N for _ in range(N)]
V = [ [-1]*N for _ in range(N)]
q = []
D = defaultdict( lambda:-1)
ans = 0
for i in range(N):
    V[i][i] = 0
for i in range(N):
    A[i] = list( map( int, input().split()))
for i in range(N):
    for j in range(i+1,N):
        heappush(q, (A[i][j], i, j))
        D[(i,j)] = A[i][j]
