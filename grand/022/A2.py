S = input()
l = len(S)
if l != 26:
    colors = [0]*26
    for i in range(l):
        colors[ ord(S[i]) - ord('a')] = 1
    for i in range(26):
        if colors[i] == 0:
            ans = S + chr( i + ord('a'))
            break
    print(ans)
elif S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
else:
    for i in range(25,0,-1):
        if S[i] > S[i-1]:
            now = i
            break
    colors = [0]*26
    for i in range(now-1):
        colors[ ord(S[i]) - ord('a')] = 1
    c = 'z'
    for i in range(now-1,26):
        if S[now-1] < S[i]:
            c = min(c, S[i])
    print(S[:now-1]+c)
