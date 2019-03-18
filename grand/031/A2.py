N = int( input())
S = input()
Q = 10**9+7
A = [1]*26
ANS = [0]*26
for i in range(N):
    s = ord(S[i]) - ord("a")
    ans = 1
    for j in range(26):
        if j != s:
            ans *= A[j]
            ans %= Q
    ANS[j] = (ANS[j] + ans)%Q
    A[s] += 1
print( sum(ANS))


