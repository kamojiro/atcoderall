from itertools import product
L, N = map( int, input().split())
X = [ int( input()) for _ in range(N)]
l = 0
r = N-1
now = 0
ansl = 0
ansr = 0

for Z in product("lr", repeat = N):
    ans = 0
    l = 0
    r = N-1
    now = 0
    for x in Z:
        if x == "l":
            ans += X[l] - now
            now = X[l]
            l += 1
        else:
            ans += L - X[r] + now
            now = -L+X[r]
            r -= 1
    print(Z, ans)
