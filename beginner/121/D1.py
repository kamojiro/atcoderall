A, B = map( int, input().split())
A -= 1
TA = [0]*41
TB = [0]*41
if A%4 == 1 or A%4 == 2:
    TA[0] = 1
if B%4 == 1 or B%4 == 2:
    TB[0] = 1
for i in range(40,0,-1):
    if 2**i <= A:
        TA[i] = (A - 2**i +1)%2
        A -= 2**i
    if 2**i <= B:
        TB[i] = (B - 2**i + 1)%2
        B -= 2**i
a = 0
b = 0
for i in range(41):
    a += TA[i]*(2**i)
    b += TB[i]*(2**i)
print(a^b)
