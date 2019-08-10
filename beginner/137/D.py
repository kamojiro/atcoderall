import sys
input = sys.stdin.readline

def main():
    N, M = map( int, input().split())
    L = [(0,0) for _ in range(N)]
    for i in range(N):
        a, b = map( int, input().split())
        L[i] = (b,a)
    L.sort(reverse = True)
    V = [0]*M
    W = [ i for i in range(M)]
    def find(A,x):
        p = A[x]
        if p == x:
            return x
        a = find(A,p)
        A[x] = a
        return a
 
    def union(A, x, y):
        #    bx, by = sorted([find(A,x), find(A,y)]) # bx, by = find(A,x), find(A,y)だと無限ループ。
        if find(A,x) > find(A,y):
            bx, by = find(A,y), find(A,x)
        else:
            bx, by = find(A,x), find(A,y)
        A[y] = bx
        A[by] = bx

    for i in range(N):
        b, a = L[i]
        t = M-a
        if t < 0:
            continue
        if V[t] == 0:
            V[t] = b
            if t > 0:
                if V[t-1] > 0:
                    union(W, t, t-1)
            if t < M-1:
                if V[t+1] > 0:
                    union(W, t, t+1)
            continue
        s = find(W,t)
        if s == 0:
            if V[0] == 0:
                V[0] = b
                if M > 1:
                    if V[1] > 0:
                        union(W, 0, 1)
        else:
            V[s-1] = b
            if s-1 > 0:
                if V[s-2] > 0:
                    union(W, s-1, s-2)
            union(W,s-1,s)
    print( sum(V))
            
            
            
            
if __name__ == '__main__':
    main()
