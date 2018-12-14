N = int( input())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
cnt = sum(B) - sum(A)
cnta = 0
cntb = 0
for i in range(N):
    a = A[i]
    if A[i] == B[i]:
        pass
    elif A[i] > B[i]:
        cntb += A[i]-B[i]
    else:
        if (B[i]-A[i])%2 == 1:
            cnta += 1
            cntb += 1
        cnta += (B[i]-A[i])//2
if cnt <= -1:
    print('No')
elif cnt >= cnta and cnt >=  cntb and cnt - cntb == 2*(cnt - cnta):
    print('Yes')
else:
    print('No')
