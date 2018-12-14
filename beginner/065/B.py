N = int( input())
A = [ int( input()) for _ in range(N)]
A = [ a-1 for a in A]
L = [ 0 for _ in range(N)]
L[0] = 1
cnt = 0
now = 0
while True:
    if now == 1:
        break
    now = A[now]
    if L[now] == 0:
        L[now] = 1
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)
