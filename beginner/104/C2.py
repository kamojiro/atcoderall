D, G = map( int, input().split())
P = []
C = []
NUM = [[] for _ in range(D)]
for i in range(D):
    p, c = map( int, input().split())
    P.append(p)
    C.append(c)
    NUM[p].append(i)
AVE = [[] for _ in range(D)]
for i in range(D):
    AVE[i].append((100*P[i]*(i+1)+C[i])/P[i])
    AVE[i].append(i)
AVE = sorted(AVE)

