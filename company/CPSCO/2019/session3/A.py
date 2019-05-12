S = input()
ans = ""
for s in S:
    if s == "A":
        ans += "O"
    elif s == "O":
        ans += "A"
    else:
        ans += s
print(ans)
