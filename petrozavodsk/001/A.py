X, Y = map( int, input().split())
if X == Y:
    ans = -1
elif X > Y:
    if X%Y == 0:
        ans = -1
    else:
        ans = X
else:
    ans = X
print(ans)










