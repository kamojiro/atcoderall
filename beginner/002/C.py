xa, ya, xb, yb, xc, yc = map( int, input().split())
X = [xa, xb, xc]
Y = [ya, yb, yc]
Z = [(xa, ya), (xb, yb), (xc, yc)]
Z.sort()
(xa, ya) = Z[0]
(xb, yb) = Z[1]
(xc, yc) = Z[2]
if (ya <= yb and yb <= yc) or (ya >= yb and yb >= yc):
    ans = abs( abs(yc - ya)*abs(xb - xa) + abs(yc - yb)*abs(xc - xa) -abs(yc-ya)*abs(xc - xa))/2
else:
    ans = ( max(X) - min (X))*( max(Y)-min(Y))
    ans -= abs( xa - xb)*abs(ya-yb)/2
    ans -= abs( xc - xb)*abs(yc-yb)/2
    ans -= abs( xa - xc)*abs(ya-yc)/2
print( ans)
