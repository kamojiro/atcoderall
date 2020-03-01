import sys
input = sys.stdin.readline
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

from collections import defaultdict
def main():
    N, M, K = map( int, input().split())
    AB = [ tuple( map( lambda x:x-1, map( int, input().split()))) for _ in range(M)]
    CD = [ tuple( map( lambda x:x-1, map( int, input().split()))) for _ in range(K)]
    fn = [0]*N
    bn = [0]*N
    df = defaultdict( lambda : False)
    friends = [ i for i in range(N)]
#    blocks = [ i for i in range(N)]
    for a, b in AB:
        fn[a] += 1
        fn[b] += 1
        df[(a,b)] = True
        df[(b,a)] = True
        union(friends,a,b)
    for c, d in CD:
#        union(blocks, c, d)
        if find(friends, c) == find( friends, d):
            if not df[(c,d)]:
                bn[c] += 1
                bn[d] += 1
    S = [-1]*N
    for i in range(N):
        S[ find( friends, i)] += 1
    ANS = [0]*N
    for i in range(N):
        ANS[i] = S[ find( friends, i)] - fn[i] - bn[i]
    print(' '.join( map( str, ANS)))
    
if __name__ == '__main__':
    main()
