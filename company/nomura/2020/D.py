#import sys
#input = sys.stdin.readline
Z = 10**9+7
from collections import Counter
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
    N = int( input())
    P = list( map( lambda x: int(x)-1, input().split()))
    Q = []
    V = [ i for i in range(N)]
    R = []
    for i in range(N):
        p = P[i]
        if p == -2:
            Q.append(i)
            continue
        R.append(i)
        union(V,i,p)
    S = set()
    for r in R:
        S.add( find(V,r))
    City = list(S)
    M = len(City)
    CV = Counter([ find(V, i) for i in range(N)])
    Block = [ CV[city] for city in City]
    d = sum([b-1 for b in Block])
    L = len(Q)
    ans = d*pow(N-1, L, Z)%Z
    # addans = 0
    # if L > 0:
    #     addans = 1
    # print(ans)
    print("defans", ans)
    print(d, CV)
    print(L, Q)
    for q in Q:
        # print(q, find(V,q))
        if CV[find(V,q)] < 2:
            print(q+1)
            ans += (pow(N-1,L,Z) - (L-1)*pow(N-1,L-2,Z))%Z
        else:
            ans += (pow(N-1,L-1,Z)*(N-CV[find(V,q)])%Z - (L-1)*pow(N-1,L-2,Z))%Z
        #     # print((N-CV[find(V,q)]))
        ans %= Z
    print(ans)
            
    
if __name__ == '__main__':
    main()
