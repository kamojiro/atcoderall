Q = int( input())
def matching(A,B):
    #最大となる組み合わせは、1,2,...,xと1,2,...,xという頂点を逆順で組み合わせることで得られることが分かる
    #このとき、これらの積の最大値は(x+1)//2*(x+1-(x+1)//2)である
    #ここで、B = A + nであるとき、最大はA*(A+(n-1))以上になることが分かる。
    #n >= 1であれば、積の最大値はA.Bを飛ばしても実現されることが分かる。
    if A == B:
        return 2*A - 2
    S = A*B
    L, H = 0, A*B
    while H - L != 1:
        M = (L+H)//2
        if ((M+1)//2)*(M + 1 - (M+1)//2) < S:
            L = M
        else:
            H = M
    return L-1 #L-1なのは、A,Bを飛ばすため
for _ in range(Q):
    A, B = map( int, input().split())
    print( matching(A,B))
