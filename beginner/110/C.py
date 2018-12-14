S = input()
T = input()
A = [-1]*26
V = [0]*26
L = len(S)
ans = 'Yes'
for i in range(L):
    print(i)
    ords = ord(S[i])-97
    ordt = ord(T[i])-97
    if A[ords] == -1 or A[ordt] == -1:
        A[ords], A[ordt] = ordt, ords
    elif A[ords] == -1 or A[ordt] == -1:
        if V[ords] == 0 and V[ordt] == 0:
             A[ords], A[ordt] = ordt, ords
        else:
            ans = 'No'
            break
    else:
        if A[ords] != ordt or A[ordt] != ords:
            ans = 'No'
            break
    V[ordt] = 1
print(ans)

        
