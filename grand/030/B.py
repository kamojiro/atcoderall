L, N = map( int, input().split())
X = [ int( input()) for _ in range(N)]
l = 0
r = N-1
now = 0
ansl = 0
ansr = 0
d = "l"
for _ in range(N):
    if X[l] - now == now + (L - X[r]):
        if d == "l":
            ansl += X[l] - now
            now = X[l]
            l += 1
        else:
            ansl += L - X[r] + now
            now = -L+X[r]
            r -= 1
    elif X[l] - now >= now + (L - X[r]):
        ansl += X[l] - now
        now = X[l]
        l += 1
        d = "l"
    else:
        ansl += L - X[r] + now
        now = -L+X[r]
        r -= 1
        d = "r"
d = "r"
l = 0
r = N-1
now = 0
for _ in range(N):
    if X[l] - now == now + (L - X[r]):
        if d == "l":
            ansr += X[l] - now
            now = X[l]
            l += 1
        else:
            ansr += L - X[r] + now
            now = -L+X[r]
            r -= 1
    elif X[l] - now >= now + (L - X[r]):
        ansr += X[l] - now
        now = X[l]
        l += 1
        d = "l"
    else:
        ansr += L - X[r] + now
        now = -L+X[r]
        r -= 1
        d = "r"
print( ansl, ansr)
print( max( ansl, ansr))
