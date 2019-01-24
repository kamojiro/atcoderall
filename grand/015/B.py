S = input()
l = len(S)
ans = 0
for i in range(l):
    if S[i] == "U":
        ans += l-1-i + i*2
    else:
        ans += (l-1-i)*2 + i
print( ans)









