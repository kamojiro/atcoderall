N = int( input())
A = [0]*N
B = [0]*N
C = [0]*N
SA = [(0,0)]*N
SB = [(0,0)]*N
for i in range(N):
    a, b = map( int, input().split())
    A[i] = a
    B[i] = b
    SA[i] = (-b,-a,i)#(-a,-abs(a-b),-a+b,-b,i)
    SB[i] = (-a,-b,i)#(-b,-abs(a-b),b-a,-a,i)
SA.sort()
SB.sort()
ansa = 0
ansb = 0
a = 0
b = 0

for i in range(N):
    if i%2 == 0:
        while 1:
           _, _,j = SA[a]
           if C[j] == 0:
                ansa += A[j]
                C[j] = 1
                a += 1
                break
           else:
                a += 1
    else:
        while 1:
            _,_,j = SB[b]
            if C[j] == 0:
                ansb += B[j]
                C[j] = 1
                b += 1
                break
            else:
                b += 1
print( ansa - ansb)
