from collections import deque
N = int( input())
D = dict()
Path = [ [] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map( int, input().split())
    a, b = a-1, b-1
    D[1000000*a+b] = c
    D[1000000*b+a] = c
    Path[a].append(b)
    Path[b].append(a)
Q, K = map( int, input().split())
foot = [ 0 for _ in range(N)]
foot[K-1] = 1
length = [ 0 for _ in range(N)]
A = deque([])
for d in Path[K-1]:
    foot[d] = 1
    A.append(d)
    length[d] = D[1000000*d + K-1]
while len(A) != 0:
    d = A.pop()
    foot[d] = 1
    for g in Path[d]:
        if foot[g] == 0:
            length[g] = length[d] + D[1000000*d + g]
            A.append(g)
for _ in range(Q):
    x, y = map( int, input().split())
    print(length[x-1]+length[y-1])
    
