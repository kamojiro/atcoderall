n, m = map( int, input().split())
Q = 10**9+7
def zen(A, k):
    jiku = 0
    l = 0
    if k%2 == 1:
        s = 1
        for i in range(k//2):
            l += s*(A[-i-1] - A[i])
            jiku += l*2
            jiku %= Q
            s *= -1
    else:
        for i in range(k//2-1):
            l += A[-i-1] - A[i]
            jiku += l*2
            jiku %= Q
        jiku += l + A[-k//2] - A[k//2-1]
        jiku %= Q
    return jiku
X = list( map( int, input().split()))
Y = list( map( int, input().split()))

print((zen(X,n)*zen(Y,m))%Q)
