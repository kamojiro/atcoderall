N = int( input())
A = [ int( input()) for _ in range(N)]
A.sort(key=None, reverse = True)
ans = A[0]
for i in range(1, N):
    if ans != A[i]:
        ans = A[i]
        break
print(ans)
