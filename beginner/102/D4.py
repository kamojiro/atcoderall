N = int( input())
A = list( map( int, input().split()))
SUM = [0]
for i in range(N):
    SUM.append(SUM[-1]+A[i])
Lnow = 1
Rnow = 2
ans = 10**10
for i in range(2, N-1):
    for j in range(Lnow, i):
        if SUM[i] - SUM[j] <= SUM[j]:
            if abs(SUM[i] - SUM[j]*2) >= abs(SUM[i] - SUM[j-1]*2):
                Lnow = j-1
            else:
                Lnow = j
            break
        else:
            Lnow = j
    for k in range( max(Rnow, i+1),N):
        print(k)
        if SUM[N] - SUM[k] <= SUM[k] - SUM[i]:
#            print('huge')
#            print('{} {}'.format(abs(SUM[N] - SUM[k] - SUM[k] + SUM[i]), abs(SUM[N] - SUM[k-1] - SUM[k-1] + SUM[i])))
            if abs(SUM[N] - SUM[k] - SUM[k] + SUM[i]) >= abs(SUM[N] - SUM[k-1] - SUM[k-1] + SUM[i]):
                Rnow = k-1
            else:
                Rnow = k
            break
        else:
            Rnow = k
    print('{} {} {} {}'.format(SUM[Lnow], SUM[i]-SUM[Lnow], SUM[Rnow] - SUM[i], SUM[N] - SUM[Rnow]))
    ans = min( ans, max(SUM[Lnow], SUM[i]-SUM[Lnow], SUM[Rnow] - SUM[i], SUM[N] - SUM[Rnow]) - min(SUM[Lnow], SUM[i]-SUM[Lnow], SUM[Rnow] - SUM[i], SUM[N] - SUM[Rnow]))
print(ans)
