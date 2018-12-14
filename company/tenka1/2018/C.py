N = int( input())
A = [ int( input()) for _ in range(N)]
ans1 = 0
A.sort()
nowL = A[0]
nowR = A[0]
for i in range(1,N):
    if i%4 == 3:
        ans1 += nowL - A[(i//4)*2+1]
        nowL = A[(i//4)*2+1]
    elif i%4 == 0:
        ans1 += nowR - A[(i//4)*2]
        nowR = A[(i//4)*2]
    elif i%4 == 1:
        ans1 += A[- (i//4)*2-1] - nowL
        nowL = A[-(i//4)*2 - 1]
    else:
        ans1 += A[- (i//4)*2 - 2] - nowR
        nowR = A[-(i//4)*2 - 2]
A = A[::-1]
ans2 = 0
nowL = A[0]
nowR = A[0]
for i in range(1,N):
    if i%4 == 1:
        ans2 += nowL - A[-(i//4)*2-1]
        nowL = A[-(i//4)*2-1]
    elif i%4 == 2:
        ans2 += nowR - A[-(i//4)*2-2]
        nowR = A[-(i//4)*2-2]
    elif i%4 == 3:
        ans2 += A[(i//4)*2+1] - nowL
        nowL = A[(i//4)*2+1]
    else:
        ans2 += A[(i//4)*2] - nowR
        nowR = A[(i//4)*2]

print( max(ans1, ans2))
