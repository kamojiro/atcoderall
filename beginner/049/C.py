T = ["dream", "dreamer","erase", "eraser", ""]
S = input()
L = len(S)
ans = "YES"
while L >= 7:
    if S[-7:] == "dreamer":
        L -= 7
        S = S[:-7]
    elif S[-6:] == "eraser":
        L -= 6
        S = S[:-6]
    elif S[-5:] == "erase" or S[-5:] == "dream":
        L -= 5
        S = S[:-5]
    else:
        ans = "NO"
        break
if S in T:
    print(ans)
else:
    print("NO") 
