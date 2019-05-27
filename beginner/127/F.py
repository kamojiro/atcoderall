import heapq
Q = int( input())
t = 0
q = []
c = 0
s = 0
for _ in range(Q):
    A = list( map( int, input().split()))
    if A[0] == 2:
        if s == t:
            print(a,b)
        m = heapq.nsmallest((t+1)//2, q)[-1]
        a, b = m, sum( list(map( abs, map( lambda x: abs(x-m), q))))+c
        print(a,b)
        s = t
    else:
        c += A[2]
        t += 1
        heapq.heappush(q, A[1])
