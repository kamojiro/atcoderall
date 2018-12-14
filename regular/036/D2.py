def find(x,A):
    p = A[x]
    if p == x:
        return x
    a = find(p, A)
    A[x] = a
    return a

def union(x, y, A):
    bx, by = find(x,A), find(y,A)
    A[y] = bx
    A[by] = bx

N, Q = map( int, input().split())
colors = [-1]*N
V = [ i for i in range(N)]
W = [i for i in range(N)]
Wnei = [ -1 for _ in range(N)]

for _ in range(Q):
    w, x, y, z = map( int, input().split())
    x, y = x-1, y-1
    if w == 2:
        if find(x, V) == find(y,V) and colors[find(x,W)] == colors[find(y,W)]:
            print('YES')
        else:
            print('NO')
    if w == 1:
        union(x,y,V)
        p, q = colors[find(x,W)], colors[find(y,W)]
        if z%2 == 0:
            if p == 2 or q == 2:
                colors[find(x,W)] = colors[find(y,W)] = 0
            elif p == -1 and q == -1:
                colors[x] = colors[y] = 0
            elif p == -1:
                colors[x] = q
            elif q == -1:
                colors[y] = p
            elif p == q:
                pass
            else:
                colors[find(p,W)] = colors[find(q,W)] = 2
            union(x,y,W)
            Wnei[find(x,W)] = Wnei[find(y,W)]
            Wnei[find(y,W)] = Wnei[find(x,W)]
        else:
            if p == 2 or q == 2:
                colors[find(x,W)] = colors[find(y,W)] = 0
            elif p == -1 and q == -1:
                colors[x], colors[y] = 0, 1
                Wnei[x] = y
                Wnei[y] = x
            elif p == -1:
                colors[x] = (q+1)%2
                Wnei[x] = find(y,W)
                union(Wnei[find(y,W)], x, W)
                if Wnei[find(y,W)] == -1:
                    Wnei[find(y,W)] = x
                else:
                    union(Wnei[find(y,W)], x, W)
                    Wnei[find(x,W)] = find(y,W)
                    Wnei[find(y,W)] = find(x,W)
            elif q == -1:
                colors[y] = (p+1)%2
                union(Wnei[find(x,W)], y, W)
                Wnei[find(y,W)] = find(x,W)
                if Wnei[find(x,W)] == -1:
                    Wnei[find(x,W)] = y
                else:
                    union(Wnei[find(x,W)], y,W)
                    Wnei[find(x,W)] = find(y,W)
                    Wnei[find(y,W)] = find(x,W)
            elif p != q:
                
            else:
                colors[find(p,W)] = colors[find(q,W)] = 2
        print(V)
        print(W)
        print(Wnei)
        print(colors)
