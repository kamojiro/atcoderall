N = int( input())
N %= 30
C = [str(i+1) for i in range(6)]
for i in range(N):
    j = i%5
    C[j], C[j+1] = C[j+1], C[j]
print( "".join(C))
