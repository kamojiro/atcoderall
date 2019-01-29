Y = int( input())
ans = "NO"
if Y%400 == 0:
    ans = "YES"
elif Y%100 == 0:
    pass
elif Y%4 == 0:
    ans = "YES"
print( ans)
