import heapq
N, K = map( int, input().split())
V = list(  map( int, input().split()))
ans = 0
for i in range(N+1):
    for j in range(N+1):
        if i + j > K or i + j > N:
            break
        cnt = i+j
        if j == 0:
            q = V[:i]
            now = sum(q)
            heapq.heapify(q)
            while q and (cnt < K):
                t = heapq.heappop(q)
                if t >= 0:
                    break
                else:
                    now += -t
                    cnt += 1
        else:
            q = V[:i] + V[-j:]
            now = sum(q)
            heapq.heapify(q)
            while q and (cnt < K):
                t = heapq.heappop(q)
                if t >= 0:
                    break
                else:
                    now += -t
                    cnt += 1
        if ans < now:
            ans = now
print( ans)
