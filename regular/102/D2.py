L = int( input())
r = 0
A = []
l = L
ANS = []
while l != 0:
    l, r = divmod(l, 2)
    A.insert(0,r)
N = len(A)
for i in range(N-1):
    ANS.append("{} {} {}".format(i+1, i+2, 0))
    ANS.append("{} {} {}".format(i+1, i+2, 2**i))
del A[0]
y = 2**(N-1)
M = 2*(N-1)
#Flag = False
for i in range(N-1):
#    if Flag == True:
#        y += A[i]*(2**(N-i-1))
    if A[i] == 1:
        ANS.append("{} {} {}".format(N-i-1, N, y))
        M += 1
        y += A[i]*(2**(N-i-2))
#        Flag = True
print("{} {}".format(N, M))
for a in ANS:
    print(a)
