L, N = map( int, input().split())
X = [ int( input()) for _ in range(N)]
anst = 0
l = 0
r = N-1
ans = 0
now = 0
if N > 2000:
    N = 1
for _ in range(N):
    if X[l] - now >= now + (L - X[r]):
        ans += X[l] - now
        now = X[l]
        l += 1
    else:
        ans += L - X[r] + now
        now = -L+X[r]
        r -= 1

anst = max( ans, anst)
for i in range(1,N):
    l = i
    r = N-1
    ans = X[i-1]
    now = X[i-1]
    for _ in range(N-i):
        if X[l] - now >= now + (L - X[r]):
            ans += X[l] - now
            now = X[l]
            l += 1
        else:
            ans += L - X[r] + now
            now = -L+X[r]
            r -= 1
    anst = max( ans, anst)

for i in range(1,N):
    l = 0
    r = N-1-i
    ans = L - X[N-i]
    now = -L + X[N-i]
    for _ in range(N-i):
        if X[l] - now >= now + (L - X[r]):
            ans += X[l] - now
            now = X[l]
            l += 1
        else:
            ans += L - X[r] + now
            now = -L+X[r]
            r -= 1
    anst = max( ans, anst)
print(anst)
