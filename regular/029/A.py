from itertools import product
N = int(input())
T = [ int(input()) for i in range(N) ]
ans = sum(T)
for x in product(range(2),repeat = N):
    ichi = 0
    ni = 0
    for i in range(N):
        if x[i] == 0:
            ichi += T[i]
        else:
            ni += T[i]
    ans = min(ans, max(ichi,ni))
print(ans)
            


