from collections import deque
N = int( input())
P = [0]*N
H = [0]*N
E = [ [] for _ in range(N)]
for i in range(1,N):
    p, h = map( int, input().split())
    P[p] = i
    E[i].append(p)
