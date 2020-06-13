import sys
import numpy as np

MOD = 998244353

N, S = map( int, input().split())
A = list( map( int, input().split()))

U = 3010

f = np.zeros(U+1, np.int64)
f[0] = 1
print(f[:10])
for a in A:
    ff = 2 * f
    print(ff[:10])
    print("a:",ff[a:], ff[a:].shape)
    print("-a:",ff[:-a], ff[:-a].shape)
    ff[a:] += f[:-a]
    ff %= MOD
    f = ff
    print(f[:10])

print(f[S])
