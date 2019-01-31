import heapq
N = int( input())
A = [ list( map( int, input().split())) for _ in range(N)]
Q = []
for i in range(N-1):
    for j in range(i+1,N):
        heapq.heappush(Q, [A[i][j],i,j])
WF = [ [10**9+1]*N for _ in range(N)]
for i in range(N):
    WF[i][i] = 0
cnt = 0
while Q:
    a, s, g = heapq.heappop(Q)
    addcheck = 1
    for i in range(N): #新しく辺(s,g)を追加できるかどうかを判断する。
        #小さい辺から順番にチェックしているので、より大きい辺との大小比較の必要がない。
        #もう一つ、最短経路が更新される可能性があるが、それは今の辺より真に大きい辺のみなので、問題ない。
        if i == s or i == g:
            continue
        else:
            if WF[s][i] + WF[i][g] == a:
                addcheck = 0
            elif WF[s][i] + WF[i][g] < a:
                 break
    else:
        WF[s][g] = a
        WF[g][s] = a
        if addcheck:
            cnt += a
        continue
    print(-1)
    break
else:
    print( cnt)
