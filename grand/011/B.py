N = int( input())
A = list( map( int, input().split()))
A.sort()
l = -1
r = N-1
while r - l > 1:
    m = (l+r)//2
    now = sum(A[:m+1])
    check = 1
    for i in range(m+1,N):
        if A[i] <= now*2:
            now += A[i]
        else:
            check = 0
            break
    if check == 1:
        r = m
    else:
        l = m
print(N-r)
        
