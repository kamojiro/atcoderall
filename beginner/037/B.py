N, Q = map( int, input().split())
ANS = [0]*N
for _ in range(Q):
    l, r, t = map( int, input().split())
    for i in range(l-1,r):
        ANS[i] = t
for ans in ANS:
    print(ans)
