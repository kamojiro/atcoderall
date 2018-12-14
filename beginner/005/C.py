T = int( input())
N = int( input())
A = list( map( int, input().split()))
M = int( input())
B = list( map( int, input().split()))
FA = [ False for _ in range(N)]
FB = [ False for _ in range(M)]
Ans = True
for i in range(M):
    b = B[i]
    for j in range(N):
        if FA[j] == False and b - A[j] <= T and A[j] <= b:
            FA[j] = True
            FB[i] = True
            break
if sum(FB) == M:
    print('yes')
else:
    print('no')
