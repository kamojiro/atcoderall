S = input()
ans = 0
a = 0
bc = 0
now = 0
for s in S:
    if s == "A":
        if now == 1:
            a = 1
            bc = 0
            now = 0
        else:
            a += 1
    elif s == "B":
        if now == 0:
            now = 1
        else:
            a = 0
            bc = 0
            now = 0
    else:
        if now == 1:
            ans += a
            now = 0
        else:
            a = 0
            bc = 0
print(ans)
