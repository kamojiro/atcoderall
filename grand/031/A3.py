from collections import Counter
N = int( input())
S = input()
Q = 10**9+7
C = Counter(S)
ans = 1
for c in C:
    ans *= C[c]+1
    ans %= Q
print((ans-1)%Q)
