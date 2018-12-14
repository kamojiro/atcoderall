S = input()
now = S[0]
cnt = 0
M = 0
nowM = 0
l = 0
L, R = 0, 0
nagasa = len(S)
for i in range( nagasa):
    if now == S[i]:
        cnt += 1
    else:
        if M < cnt:
            R = i
            L = l
            M = cnt
        elif M == cnt:
            if L == 0:
                L = l
                R = i
                M = cnt
        cnt = 1
        now = S[i]
        l = i
else:
    if M < cnt:
        R = nagasa
        L = l
        M = R-L
if L == 0 or R == nagasa:
    print(M)
else:
    print(M+1)
