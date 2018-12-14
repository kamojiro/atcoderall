import itertools

N, M = map(int, input().split())
if M == 0:
    print(1)
else:
    flg = 0
    edge = set({})
    for _ in range(M):
        x, y = map(int, input().split())
        edge.add((x,y))

    for k in range(N, 1, -1):
        allnode = set(itertools.combinations(range(1, N+1), k))
        for l in allnode:
            alledge = set(itertools.combinations(l,2))
            if alledge.issubset(edge):
                print(k)
                flg = 1
                break
        if flg == 1:
            break
