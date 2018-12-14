from itertools import product
S = list(input())
S = [int(x) for x in S]
z = [0 for _ in range(3)]
for x in product(range(2), repeat = 3):
    y = S[0]
    for i in range(1,4):
        if x[i-1] == 0:
            y += S[i]
        else:
            y -= S[i]
    if y == 7:
        z = x
        break
ans = str(S[0])
for i in range(1,4):
    if z[i-1] == 0:
        ans += '+'
    else:
        ans += '-'
    ans += str(S[i])
ans += '=7'
print(ans)
    
