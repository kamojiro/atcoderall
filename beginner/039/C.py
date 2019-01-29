S = input()
B = "WBWBWWBWBWBW"*6
if B[:20] == S:
    ans = "Do"
elif B[2:22] == S:
    ans = "Re"
elif B[4:24] == S:
    ans = "Mi"
elif B[5:25] == S:
    ans = "Fa"
elif B[7:27] == S:
    ans = "So"
elif B[9:29] == S:
    ans = "La"
elif B[11:31] == S:
    ans = "Si"
print( ans)
