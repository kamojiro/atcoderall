from collections import Counter
S = input()
C = Counter(S)
now = C[S[0]]
check = "Yes"
for s in C:
    if now != C[s]:
        check = "No"
        break
print(check)
