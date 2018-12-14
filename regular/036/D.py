def find(x,A):
    p = A[x]
    if p == x:
        return x
    a = find(p, A)
    A[x] = a
    return a

N, Q = map( int, input().split())
colors = [-1]*N
V = [ i for i in range(N)]
W = [i for i in range(N)]
Wnei = [ 0 for _ in range(N)]

for _ in range(Q):
    w, x, y, z = map( int, input().split())
    x, y = x-1, y-1
    if w == 1:
        bx, by = find(x,V), find(y,V)
        V[by] = bx
        V[y] = bx
        p, q = find(x, W), find(y,W)
        if colors[p] == -1:
            p, q = q, p
        if colors[p] == -1 and colors[q] == -1:
            if z%2 == 0:
                W[q] = p
                colors[p] = 0
            else:
                colors[p] = 0
                colors[q] = 1
                Wnei[p] = q
                Wnei[q] = p
        elif colors[q] == -1:
            if z%2 == 0:
                bp, bq = find(p,W), find(q,W)
                W[q] = bp
                W[bq] = bp
                Wnei[bp] = Wnei[bq]
            else:
                W[q] = (W[p]+1)%2
                Wnei[q] = p
                Wnei[p] = find(q,W)
        elif colors[p] == colors[q]:
            if z%2 == 1:
                bp, bq = find(p,W), find(q,W)
                W[q] = bp
                W[bq] = bp
        else:
            if z%2 == 0:
                bp, bq = find(p,W), find(q,W)
                W[q] = bp
                W[bq] = bp
    else:
        if find(x,V) == find(y,V) and find(x,W) == find(y,W):
            print('YES')
        else:
            print('NO')
