Q = 10**9 + 7
def zen(A,k):
    jiku = 0
    for i in range(k):
        jiku += i*A[i] - (k-1-i)*A[i]
    return jiku%Q
n, m = map( int, input().split())
X = list(map( int, input().split()))
Y = list(map( int, input().split()))
ans = zen(X,n)*zen(Y,m)
ans %= Q
print(ans)
