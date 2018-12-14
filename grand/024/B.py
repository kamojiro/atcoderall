N = int( input())
W = [0]*(N+1)
for _ in range(N):
    p = int( input())
    if W[p-1] >= 1:
        W[p] = W[p-1]+1
    if W[p] == 0:
        W[p] = 1
print(N - max(W))
