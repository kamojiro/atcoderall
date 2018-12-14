from collections import Counter
S = input()
T = input()
E = [ set() for _ in range(26)]
V = [0]*26
L = len(S)
ans = 'Yes'
for i in range(L):
    ords = ord(S[i])-97
    ordt = ord(T[i])-97
    E[ords] = ordt
C = Counter(E)
for x in C:
    if C[x] >= 2:
        ans = 'No'
if ans == 'Yes':
    for i in range(26):
        if V[i] == 1:
            continue
        a = i
        V[i] = 1
        while True:
            a = V[a]
            if a == i:
                break
            if V[a] == 1:
                ans = 'No'
                break
            else:
                V[a] = 1
print(ans)










