N, M = map( int, input().split())
edges = [[] for _ in range(N)]
for i in range(M):
    a, b = map( int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
vertices = [ False for _ in range(N)]
ans = 0

def dfs(p,b):
    vertices[p] = True
    bool = False
    for k in edges[p]:
        if k != b:
            if vertices[k] == True:
                return True
            else:
                bool |= dfs(k,p)
    return bool

for i in range(N):
    if vertices[i] == False:
        component = dfs(i,-1)
        if component == False:
            ans += 1
print(ans)
