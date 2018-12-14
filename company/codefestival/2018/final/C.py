from bisect import bisect_right, bisect_left
N = int( input())
P = [(0,0) for _ in range(N)]
Q = [0]*(N)
for i in range(N):
    a, b = map( int, input().split())
    P[i] = (a,b)
    Q[i] = a
    
M = int( input())
P.sort()
Q.sort()

for _ in range(M):
    t = int( input())
    j = bisect_right(Q, t)
    if j == N:
        i = N - 1
    elif j == 0:
        i = j
    elif Q[j] > t:
        i = j-1
    a, b = P[i]

    if j == 0:
        print(b)
    elif i == N -1:
        print(b + t - a)
    else:
        _, d = P[i+1]
        print( min(b+t-a,d ))
