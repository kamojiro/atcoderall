import sys
input = sys.stdin.readline

Q = 10**9+7

def subtrees(N, E, v):
    # N: vertex
    # E: edges
    # v: one vertex
    # return: directed edges adopted to tree dp
    from collections import deque
    ret_first = deque()
    ret_second = deque()
    V = [False]*N
    d = deque([v])
    while d:
        t = d.popleft()
        if V[t]:
            continue
        else:
            V[t] = True
        for e in E[t]:
            if not V[e]:
                d.append(e)
                ret_first.appendleft((t,e))
                ret_second.append((e,t))
    return list(ret_first) + list(ret_second)

# def get_number_of_vertex_with_subtrees(E, subtrees):
#     # E: edges
#     # subtrees: directed edges adopted to tree dp
#     from collections import defaultdict
#     d = defaultdict( lambda: 1)
#     for s, t in subtrees:
#         for v in E[t]:
#             if v == s:
#                 continue
#             d[(s,t)] += d[(t,v)]
#     return d

def getInv(N):
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

def factorials(N):
    invs = getInv(N)
    factorials = [1]
    inv_factorials = [1]
    for i in range(N):
        factorials.append( factorials[-1]*(i+1)%Q)
        inv_factorials.append( inv_factorials[-1]*invs[i+1]%Q)
    return factorials, inv_factorials

def main():
    from collections import defaultdict
    N = int( input())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map( lambda x: int(x)-1, input().split())
        E[a].append(b)
        E[b].append(a)
    subtree = subtrees(N,E,0)
    # num_subtree = get_number_of_vertex_with_subtrees(E, subtree)
    num_subtree = defaultdict( lambda: 1)
    F, G = factorials(N)
    d = defaultdict( int)
    for s, t in subtree:
        z = 1
        count = 0
        for v in E[t]:
            if v == s:
                continue
            num_subtree[(s,t)] += num_subtree[(t,v)]
            count += num_subtree[(t,v)]
            z *= G[num_subtree[(t,v)]]
            z %= Q
            z *= d[(t,v)]
            z %= Q
        z *= F[count]
        z %= Q
        d[(s,t)] = z
    ANS = []
    for v in range(N):
        z = 1
        count = 0
        for e in E[v]:
            count += num_subtree[(v,e)]
            z *= G[num_subtree[(v,e)]]
            z %= Q
            z *= d[(v,e)]
            z %= Q
        z *= F[count]
        z %= Q
        ANS.append(z)

    print( "\n".join( map( str, ANS)))
    
if __name__ == '__main__':
    main()
