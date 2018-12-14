from itertools import combinations
D, G = map( int, input().split())
P = []
C = []
for i in range(D):
    p, c = map( int, input().split())
    P.append(p)
    C.append(c)
SUM = []
for i in range(D):
    SUM.append(P[i]*100*(i+1) + C[i])
for k in range(1,D+1):
    for X in combinations(range(D),k):

