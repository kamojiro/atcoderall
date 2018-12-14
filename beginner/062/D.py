import heapq
N = int( input())
A = list( map( int, input().split()))
fsum = [0]*(N+1)
bsum = [0]*(N+1)
forward = A[:N]
back = A[2*N:]
back = list(map( lambda x:-x, back))
heapq.heapify(forward)
heapq.heapify(back)
fsum[0] = sum(forward)
fsumnow = fsum[0]
bsum[N] = -sum(back)
bsumnow = bsum[N]
for i in range(1,N+1):
    heapq.heappush(forward, A[N+i-1])
    fsumnow += A[N+i-1]
    fsumnow -= heapq.heappop(forward)
    fsum[i] = fsumnow
    heapq.heappush(back, -A[2*N-i])
    bsumnow += A[2*N-i]
    bsumnow += heapq.heappop(back)
    bsum[N-i] = bsumnow
ans = fsum[0] - bsum[0]
for i in range(1,N+1):
    ans = max(ans, fsum[i] - bsum[i])
print(ans)
    
    
