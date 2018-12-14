import heapq
N, K = map( int, input().split())
H = [tuple( map( int, input().split())) for _ in range(N)]
ans = 0
heapq.heapify(H) #heap型にする
for _ in range(K):
    M = heapq.heappop(H) #最小のものを取り出す
    a, b = M[0], M[1]
    ans += a
    heapq.heappush(H,(a+b,b)) #加算したものをheapに追加する
print(ans)
