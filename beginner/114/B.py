S = input()
l = len(S)
ans = 100000
for i in range(l-2):
    ans = min( ans, abs(753 - int( S[i:i+3])))
print(ans)
