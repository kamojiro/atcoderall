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

def main():
    N, M = map( int, input().split())
    U = [ i for i in range(N)]
    AB = [ tuple( map( lambda x: int(x)-1, input().split())) for _ in range(M)]
    for a, b in AB:
        union(U, a, b)
    T = [0]*N
    for i in range(N):
        T[find(U, i)] += 1
    print(max(T))
if __name__ == '__main__':
    main()
