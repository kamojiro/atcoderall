s = input()
ans = ""
for t in s:
    if t == "0":
        ans += "0"
    elif t == "1":
        ans += "1"
    else:
        ans = ans[:-1]
print(ans)
