A, B = map( int, input().split())
A_2adic = []
B_2adic = []
A = max(0, A-1)
for _ in range(41):
    A_2adic.append(A%2)
    A //= 2
    if A == 0:
        break

for _ in range(41):
    B_2adic.append(B%2)
    B //= 2
    if B == 0:
        break
a = 0
b = 0
la = len(A)
lb = len(B)
aodd = 0
bodd = 0
i = 0
for s in A_2adic:
    a += (s^aodd)*(2**i)
    aodd |= s
    i += 1
i = 0
for t in B_2adic:
    b += (t^bodd)*(2**i)
    aodd |= t
    i += 1
print(a^b)
