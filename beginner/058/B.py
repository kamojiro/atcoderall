O = input()
E = input()
L = len(O)
K = len(E)
ans = ''
for i in range(K):
    ans += O[i]+E[i]
if L != K:
    ans += O[L-1]
print(ans)










