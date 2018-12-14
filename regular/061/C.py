from itertools import product
S = [int(x) for x in list(input())]
N = len(S)
ans = 0
c = S[0]
for x in product(range(2), repeat = N-1):
    for i in range(1,N):
        if x[i-1] == 0:
            c = c*10 + S[i]
        else:
            ans += c
            c = S[i]
    ans += c
    c = S[0]
print(ans)
