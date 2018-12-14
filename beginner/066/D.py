Q = 10**9+7
n = int( input())
A = list( map( int, input().split()))
Flag = False
for i in range(n):
    if A[i] == A[i+1]:
        Flag = True
        break
if n==1:
    print(2)
elif Flag:
    print( (pow(2,n-1,Q)*4%Q -2)%Q)
else:
    print( (pow(2,n-1,Q)*4%Q -1)%Q)
