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
        s = S[i] + n #BITで扱えるようにするために、nを加算した
        invs += sums(B, s) #i<j
        add(B, s, n*2)
    return invs

N = int( input())
A = list( map( int, input().split()))
R = max(A)+1
L = 0
c = (N*(N+1)//2 + 1)//2
while R - L > 1:
    M = (R+L)//2
    S = [0]*(N+1)
    for i in range(1,N+1):
        if A[i-1] >= M:
            S[i] = S[i-1] + 1
        else:
            S[i] = S[i-1] - 1
    if invnumber(N+1,S) >= c:
        L = M
    else:
        R = M
print(L)
