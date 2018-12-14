X, Y = map( int, input().split())
ans = "Yes"
if X > Y:
    X, Y = Y, X
if (Y-X)%2 == 1:
    ans = "No"
z = (Y-X)//2
X = X -  z
Y = Y - z*3
if X < 0 or Y < 0:
    ans = "No"
if X%4 == 0 and X == Y:
    pass
else:
    ans = "No"
print(ans)
