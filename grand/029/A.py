from collections import Counter
S = input()
L = len(S)
n = Counter(S)['B']
now = 0
ans = 0
for i in range(L):
    if S[i] == 'B':
        continue
    if S[i] == 'W':
        ans += i - now
        now += 1
print(ans)
