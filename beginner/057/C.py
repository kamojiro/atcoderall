N = int( input())
ans = len( str(N))
for i in range(1,int( N**(1/2))+1):
    if N%i == 0:
        ans = min( ans, max( len( str(i)), len( str(N//i))))
print(ans)
