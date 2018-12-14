from collections import Counter
n = int( input())
alpha = [51]*26
for _ in range(n):
    S = Counter( input())
    for i in range(97,97+26):
        alpha[i-97] = min(alpha[i-97],S[chr(i)])
ans = ''
for i in range(97,97+26):
    if alpha[i-97] == 51:
        continue
    ans += chr(i)*alpha[i-97]
print(ans)
    
