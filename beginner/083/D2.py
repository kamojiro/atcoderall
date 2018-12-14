S = input()
N = len(S)
ans = N
for i in range(N-1):
    if not S[i] == S[i+1]:
        ans = min( ans, max(N-1-i, i+1))
print(ans)
