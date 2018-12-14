N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
A = sorted(A)
ans = 0
K = A[0]
cnt = 0
for i in range(N):
    if A[i] == K:
        cnt = (cnt + 1)%2
    else:
        K = A[i]
        ans += cnt
        cnt = 1
if A[N-1] == K:
    ans += cnt
print(ans)
