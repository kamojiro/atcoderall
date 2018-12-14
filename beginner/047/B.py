w, h, n = map( int, input().split())
l = 0
r = w
d = 0
u = h
for _ in range(n):
    x, y, a = map( int, input().split())
    if a == 1:
        l = max(l,x)
    elif a == 2:
        r = min(r,x)
    elif a == 3:
        d = max(d,y)
    else:
        u = min(u,y)
if r-l <= 0 or u-d <= 0:
    print(0)
else:
    print(max(0,(r-l)*(u-d)))
