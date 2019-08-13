import sys
input = sys.stdin.readline

def main():
    N, M, P = map( int, input().split())
    d = dict()
    for _ in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        d[(a,b)] = P-c

    V = [None]*N
    V[0] = 0
    for _ in range(N-1):
        for e in d:
            s, t = e
            if V[s] == None:
                continue
            if V[t] == None:
                V[t] = V[s] + d[e]
                continue
            if V[s] + d[e] < V[t]:
                V[t] = V[s] + d[e]
    W = [V[i] for i in range(N)]
    for e in d:
        s, t = e
        if V[s] == None:
            continue
        if V[t] == None:
            V[t] = V[s] + d[e]
            continue
        if V[s] + d[e] < V[t]:
            V[t] = V[s] + d[e]
    for i in range(N):
        if V[i] == None or W[i] == None:
            continue
        if V[i] < W[i]:
            V[i] = "a"
    for _ in range(N):
        for e in d:
            s, t = e
            if V[s] == "a" or V[t] == "a":
                V[t] == "a"
                continue
            if V[s] == None:
                continue
            if V[t] == None:
                V[t] = V[s] + d[e]
                continue
            if V[s] + d[e] < V[t]:
                V[t] = V[s] + d[e]
    # ans = V[N-1]
    # for _ in range(N):
    #     for e in d:
    #         s, t = e
    #         if V[s] + d[e] < V[t]:
    #             V[t] = V[s] + d[e]

    # if V[N-1] < ans:
    #     print(-1)
    #     return
    # print( max(-ans,0))
    if V[-1] == "a":
        print(-1)
    else:
        print(max(-W[-1],0))
if __name__ == '__main__':
    main()
