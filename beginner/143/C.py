N = int( input())
S = input()
ans = 1
now = S[0]
for i in range(1, N):
    if now == S[i]:
        continue
    now = S[i]
    ans += 1
print(ans)    










