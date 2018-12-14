S = input()
l = len(S)
colors = [0]*26
for s in S:
    colors[ ord(s) - ord('a')] = 1
check = 1
if not l == 26:
    for i in range(26):
        if colors[i] == 0:
            ans = S + chr(i+ord('a'))
            break
else:
    check = 0
    now = ord("a")-1
    for i in range(25,-1,-1):
        if ord(S[i]) < now:
            colors = [0]*26
            for j in range(i):
                colors[ord(S[i]-ord('a'))] = 1
            for j in range(26):
                if colors[j] == 0:
                    ans = S[:i] + 
            ans = S[:i]+S[-1]
            check = 1
            break
        else:
            now = ord(S[i])
if check:
    print(ans)
else:
    print(-1)
