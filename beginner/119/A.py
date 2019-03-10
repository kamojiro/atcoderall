y, m, d = map( int, input().split("/"))
ans = "TBD"
if y <= 2018:
    ans = "Heisei"
elif y == 2019:
    if m <= 3:
        ans = "Heisei"
    elif m == 4:
        if d <= 30:
            ans = "Heisei"
print( ans)
