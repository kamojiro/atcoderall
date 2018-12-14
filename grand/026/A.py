N = int(input())
A = list(map(int,input().split()))
stan = A[0]
ans = 0
k = 0
for i in range(1,N):
    if stan == A[i]:
        ans += 1 + k
        k = -((k-1)%2)
    else:
        k = 0
    stan = A[i]
print(ans)
        
    
