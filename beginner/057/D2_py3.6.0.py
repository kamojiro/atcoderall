from math import factorial
from collections import Counter
def combination(a,b):
    if a < b:
        a, b = b, a
    comb = 1
    for i in range(b):
        comb *= a-i
    comb //= factorial(b)
    return comb

N, A, B = map( int, input().split())
V = list( map( int, input().split()))
V.sort( reverse = True)
print( sum(V[:A])/A)
CV = Counter(V)
ans = 0
K = CV[ max(V)]
if A <= K:
    for i in range(A, min(K, B)+1):
        ans += combination(K, i)
else:
    cnt = A
    for x in CV:
        if cnt <= CV[x]:
            ans += combination(CV[x],cnt)
            break
        else:
            cnt -= CV[x]
print(ans)
