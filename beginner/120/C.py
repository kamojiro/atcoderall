S = input()
r = 0
ans = 0
T = []
for s in S:
    if T:
        if not (T[-1] == s):
            T.pop(-1)
            ans += 2
        else:
            T.append(s)
    else:
        T.append(s)
print(ans)
        
