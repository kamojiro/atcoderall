S = list( input())
L = len(S)
R = [0]*(L+1)
for i in range(1,L+1):
    if S[i-1] == '(':
        if R[i-1] == -1:
            R[i] = 1
        else:
            R[i] = R[i-1]+1
    else:
        if R[i-1] == -1:
            R[i-1] = -1
        else:
            R[i] = R[i-1]-1
K = [0]*(10**5+1)
ans = 0
for i in range(L):
    if S[i] == ')':
        if R[i+1] == -1:
            K = [0]*(10**5+1)
            pass
        else:
            ans += K[R[i+1]]
    else:
        if R[i+1] == -1:
            K = [0]*(10**5+1)
        else:
            K[R[i+1]-1] += 1
print(ans)
    
    
