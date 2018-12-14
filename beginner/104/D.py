S = input()
L = len(S)
Q = 10**9 + 7
anum = [ 0 for _ in range(L+1)] #i番目までのAの個数の合計
cnum = [ 0 for _ in range(L+1)] #i番目までのCの個数の合計
hnum = [ 0 for _ in range(L+1)] #i番目までの?の個数の合計
for i in range(1,L+1):
    if S[i-1] == 'A':
        anum[i] = anum[i-1] + 1
        cnum[i] = cnum[i-1]
        hnum[i] = hnum[i-1]
    elif S[i-1] == 'B':
        anum[i] = anum[i-1]
        cnum[i] = cnum[i-1]
        hnum[i] = hnum[i-1]
    elif S[i-1] == 'C':
        anum[i] = anum[i-1]
        cnum[i] = cnum[i-1] + 1
        hnum[i] = hnum[i-1]
    else:
        anum[i] = anum[i-1]
        cnum[i] = cnum[i-1]
        hnum[i] = hnum[i-1] + 1
ans = 0
czen = cnum[L] #全部のCの個数
hzen = hnum[L] #全部の?の個数
for i in range(1,L+1):
    if S[i-1] == 'B' or S[i-1] == '?':
        A = ((anum[i-1]*pow(3,hnum[i-1],Q))%Q + (hnum[i-1]*pow(3,max(0,hnum[i-1]-1),Q))%Q)%Q
        C = (((czen - cnum[i])*pow(3,hzen - hnum[i],Q))%Q + ((hzen - hnum[i])*pow(3,max(0,hzen - hnum[i]-1),Q))%Q)%Q
        K = (A*C)%Q
        ans = (ans + K)%Q
print(int(ans))
