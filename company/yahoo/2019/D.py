from itertools import accumulate
L = int( input())
A = [ int( input()) for _ in range(L)]
sumA = sum(A)
accA = accumulate(A)
AO = [ a%2 for _ in range(L)]
ans = L - sum(AO) - (1- A[0]) - (1-A[1])
fcheck = [L+1]*(L+1)
fcheck[0] = sumA
now = L - sum(AO) - (1- A[0]) - (1-A[1])
mim = sumA
mimind = 0
for i in range(L):
    if AO[i+1] == 0:
        now -= 1
    else:
        
now = mim
for i in range(mim+1):
    
    if i == 0:
        

        
