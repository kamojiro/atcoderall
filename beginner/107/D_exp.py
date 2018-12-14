def add(B,a,n):#リストに値を追加する関数
    x = a
    while x <= n:
        B[x] += 1
        x += x&(-x)

def sums(B,a):#a番目までの和
    x = a
    S = 0
    while x != 0:
        S += B[x]
        x -= x&(-x)
    return S


def invnumber(n, S):# #{(i,j)| i<j and S[i]<=S[j]}
    B = [0]*(n*2 + 1)
    invs = 0
    for i in range(n):
        s = S[i] + n
        invs += sums(B, s)
        add(B, s, n*2)
    invs += sums(B, n*2)
    return invs


S = list( map( int, input().split()))
print( invnumber( len(S), S))
