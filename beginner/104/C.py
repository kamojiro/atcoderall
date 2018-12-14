D, G = map( int, input().split())
P = []
C = []
NUM = [[] for _ in range(D)]
for i in range(D):
    p, c = map( int, input().split())
    P.append(p)
    C.append(c)
    NUM[p].append(i)
SUM = []
for i in range(D):
    SUM.append(P[i]*100*(i+1) + c[i])
now = 0
cnt = 0
ans = 0
while now < G:
    cnt += 1
    ans += 1
    if cnt in P:
        
        
        
        
