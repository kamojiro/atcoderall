from copy import deepcopy
N, M = map( int, input().split())
E = [ list( map( int, input().split())) for _ in range(M)]
'''
X = [set() for _ in range(1,N+1)]
for i in range(M):
    a, b = map( int, input().split())
    X[a] = set([b])
    X[b] = set([a])
'''
vertices = [0 for _ in range(N)]

def treecomp(E,vertices):
    tree = True
    Edge = deepcopy(E)
    v = vertices[0]
    S = set()
    T = [v]
    while len(T) != 0:
        for 
            if x in S:
                tree = False
            else:
                S.add(x)
    
            
                
    return comp, vertices

vertices = [0 for _ in range(1,N+1)]
