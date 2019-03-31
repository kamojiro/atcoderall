N, X = map( int, input().split())
S = list( map( int, input().split()))

from itertools import permutations
c = 0
for p in permutations( range(N)):
    x = X
    ans = []
    for i in range(N):
        x %= S[p[i]]
        ans.append(x)
    c += x
    print(ans)
print(x)


