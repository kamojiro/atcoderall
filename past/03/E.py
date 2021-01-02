#import sys
#input = sys.stdin.readline
def main():
    N, M, Q = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map( lambda x: int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)
    V = list( map( int, input().split()))
    S = [ tuple( map( int, input().split())) for _ in range(Q)]
    ANS = []
    for s in S:
        if s[0] == 2:
            ANS.append(V[s[1]-1])
            V[s[1]-1] = s[2]
            continue
        x = s[1]-1
        ANS.append(V[x])
        c = V[x]
        for v in E[x]:
            V[v] = c
    print("\n".join( map( str, ANS)))
    
if __name__ == '__main__':
    main()
