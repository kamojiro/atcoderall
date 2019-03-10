from itertools import accumulate
L = int( input())
A = [ int( input()) for _ in range(L)]
sumA = sum(A)
accA = accumulate(A)
AO = [ a%2 for _ in range(L)]
ans = L - sum(AO) - (1- A[0]) - (1-A[1])
l = 0
lodd = AO[0]
r = 0
rodd = AO[0]
now = sumA
while :
    
fcheck = [L+1]*(L+1)
fcheck[0] = sumA
now = sumA
mim = sumA
mimind = 0
for i in range(L):
    if i == 0:
        now -= A[i]
    if i == L-1:
        now -= A[i]
    if AO[i] == 1:
        now -= A[i]
    else:
        now -= A[i] - 1
    if now <= mim:
        mim = now
        mimindex = i+1
    fcheck[i+1] = mim
