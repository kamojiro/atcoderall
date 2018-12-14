X, Y = map( int, input().split())
ans = 1
now = X
Flag = True
while Flag:
    now = 2*now
    if now <= Y:
        ans += 1
    else:
        Flag = False
print(ans)
