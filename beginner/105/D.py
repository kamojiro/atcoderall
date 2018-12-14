N, M = map( int, input().split())
A = list( map( int, input().split()))
A = [ x%M for x in A]
SUM = [0]
for i in range(N):
    SUM.append(SUM[-1]+A[i])
ans = 0
cnt = 1
for l in range(N):
    if A[l] == 0:
        ans += cnt
        cnt += 1
    else:
        PART = 0
        for r in range(l+1,N+1):
            if (SUM[r] - SUM[l])%M == 0:
                PART += 1
        ans += cnt * PART
        cnt = 1
print(int(ans))
