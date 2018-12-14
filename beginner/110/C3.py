S = input()
T = input()
A = [-1]*26
B = [-1]*26
L = len(S)
ans = 'Yes'
for i in range(L):
    ords = ord(S[i])-97
    ordt = ord(T[i])-97
    if A[ords] == -1 and B[ordt] == -1:
        A[ords] = ordt
        B[ordt] = ords
    elif A[ords] == ordt and B[ordt] == ords:
        continue
    else:
        ans = 'No'
print(ans)

        
