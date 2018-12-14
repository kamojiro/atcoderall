from collections import deque
N, K = map( int, input().split())
A = list( map( int, input().split()))
q = deque( maxlen=K)
q.append(0)
ans = 0
for i in range(N):
    a = A[i]
    while A[q[-1]] >= a:
        q.pop()
        if not q:
            break
    q.append(i)
    if i-K >= q[0]:
        q.popleft()
    ans += A[q[0]]
print(ans)
