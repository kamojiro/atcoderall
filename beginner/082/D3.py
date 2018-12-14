S = input()
x, y = map( int, input().split())
c = 0
ver = []
row = []
l = 0
for s in S:
    if s == "F":
        c += 1
    else:
        if l%2 == 0:
            row.append(c)
        else:
            ver.append(c)
        l += 1
        c = 0
if l%2 == 0:
    row.append(c)
else:
    ver.append(c)

x -= row.pop(0)
row.sort( key = None, reverse = True)
ver.sort( key = None, reverse = True)
nx, ny = 0, 0
for a in row:
    if a >= 0:
        if nx <= x:
            nx += a
        else:
            nx -= a
    else:
        if nx > x:
            nx += a
        else:
            nx -= a
for a in ver:
    if a >= 0:
        if ny <= y:
            ny += a
        else:
            ny -= a
    else:
        if ny > y:
            ny += a
        else:
            ny -= a

if x == nx and y == ny:
    print("Yes")
else:
    print("No")

#dpっぽい
