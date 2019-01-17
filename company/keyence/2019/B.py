S = input()
L = len(S)
ans = "NO"
for i in range(8):
    if S[:i] + S[i-7:] == "keyence":
        ans = "YES"
print(ans)
