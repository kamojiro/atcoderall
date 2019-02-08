from itertools import accumulate
N = int( input())
A = list( map( int, input().split()))
A.sort()
l = -1
r = N-1
B = list( accumulate(A))
while r - l > 1:
    m = (l+r)//2
    check = 1
    #now = sum(A[:m+1])
    for i in range(m+1,N):
        if A[i] <= B[i-1]*2:
            pass
        # if A[i] <= now*2:
        #     now += A[i]
        else:
            check = 0
            break
    if check == 1:
        r = m
    else:
        l = m
print(N-r)
        
