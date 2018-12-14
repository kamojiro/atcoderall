from collections import defaultdict
def find(x, A): #unionfind
    p = A[x]
    if p == x:#根になっていればよい
        return x
    a = find(p, A)#根はない場合は根に到達するまで再帰的にfindする。この1行で少し最適化される
    A[x] = a
    return a

N, K, L = map( int, input().split())
V = [ i for i in range(N)]#道路
W = [ i for i in range(N)]#鉄道
for _ in range(K):#道路
    p, q = map( int, input().split())
    p, q = p-1, q-1
    bp, bq = find(p,V), find(q,V)
    V[q] = bp#pの根bpにqとqの根bpをくっつける
    V[bq] = bp

for _ in range(L):#鉄道
    r, s = map( int, input().split())
    r, s = r-1, s-1
    br, bs = find(r,W), find(s,W)
    W[s] = br#rの根brにsとsの根bsをくっつける
    W[bs] = br

d = defaultdict(int) #デフォルトで0を返すdict。
for i in range(N):
    d[(find(i,V), find(i, W))] += 1
ANS = [0]*N

for i in range(N):
    ANS[i] = d[(find(i,V), find(i, W))]

print(' '.join( map( str, ANS)))
    
