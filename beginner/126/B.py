t = input()
a = int( t[0])*10+int(t[1])
b = int( t[2])*10 + int( t[3])
if 1 <= a <= 12:
    if 1 <= b <= 12:
        ans = "AMBIGUOUS"
    else:
        ans = "MMYY"
else:
    if 1 <= b <= 12:
        ans = "YYMM"
    else:
        ans = "NA"
print(ans)









