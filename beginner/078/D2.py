N, Z, W = map( int, input().split())
A = list( map( int, input().split()))

valZ = Z
valW = W
now = 0
t = 0
while 1:
    if t == 0:
        maxA = max(A[now:])
        if maxA == A[-1]:
            valZ = maxA
            break
        else:
            for i in range(N-1,now-1,-1):
                if maxA == A[i]:
                    now = i
                    valZ = A[i]
                    break
    else:
        minA = min(A[now:])
        if minA == A[-1]:
            valW = minA
            break
        else:
            for i in range(N-1,now-1,-1):
                if minA == A[i]:
                    now = i
                    valW = A[i]
                    break
    t = (t+1)%2
print( abs(valZ - valW))
