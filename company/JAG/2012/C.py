from heapq import *
from statistics import median

def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a

def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx
while True: 
    n, m = map( int, input().split())
    if n == 0 and m == 0:
        break
    H = [(0,0,0)]*m
    C = []
    for i in range(m):
        s, t, c = map( int, input().split())
        H[i] = (c,s-1,t-1)
        V = [ i for i in range(n)]
    heapify(H)
    while H:
        c,s,t = heappop(H)
        if find(V,s) != find(V,t):
            union(V,s,t)
            C.append(c)
    print(median(C))
