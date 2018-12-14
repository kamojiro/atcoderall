S = list(input())
T = list("AKIHABARA")
ans = "YES"
i = 0
while i < len(S) and i < 9:
    if S[i] != T[i]:
        if T[i] == "A":
            S.insert(i,"A")
    i += 1
if S[-1] != "A":
    S += "A"

if S == T:
    print("YES")
else:
    print("NO")
