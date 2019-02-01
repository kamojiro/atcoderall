s = input()
N = len( s)
ans = 0
l = 0
r = N-1
while l < r:
    lx = 0
    rx = 0
    while l <= N-1:
        if s[l] == "x":
            lx += 1
            l += 1
        else:
            break
    while 0 <= r:
        if s[r] == "x":
            rx += 1
            r -= 1
        else:
            break
    if l == r:
        ans += abs( lx - rx)
    if l < r:
        if s[l] == s[r]:
            ans += abs(lx - rx)
        else:
            ans = -1
            break
    l += 1
    r -= 1
print( ans)
