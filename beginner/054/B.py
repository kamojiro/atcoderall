N, M = map( int, input().split())
A = ['']*N
B = ['']*M
for i in range(N):
    a = input()
    A[i] = a
for i in range(M):
    b = input()
    B[i] = b
k=N-M+1
ans = 'No'
for i in range(k):
    for j in range(k):
        now = 1
        for l in range(M):
            if not A[i+l][j:j+M] == B[l]:
                now = -1
                break
        if now == 1:
            ans = 'Yes'
            break
    if ans == 'Yes':
        break
print(ans)
    
