N, M = map( int, input().split())
V = [set([]) for _ in range(N)]
E = []
for i in range(M):
    a, b = map(int, input().split())
    E.append([a-1,b-1])
    V[a-1].add(b-1)
    V[b-1].add(a-1)
ans = 0
def conn(a,b,V):
    TV = [ False for _ in range(N)]
    TV[a] = True
    S = []
    for v in V[a]:
        if v != b:
            S.append(v)
    while len(S) != 0:
        c = S.pop()
        for w in V[c]:
            if TV[w] == False:
                TV[w] = True
                S.append(w)
    return TV
for e in E:
    a, b = e[0], e[1]
    comp = conn(a,b,V)
    if comp[b] == False:
        ans += 1
print(ans)
    
    

