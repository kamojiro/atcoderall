#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    Q = int( input())
    Query = [ tuple( map( int, input().split())) for _ in range(Q)]
    t = 0
    G = [i for i in range(N+1)]
    R = [i for i in range(N+1)]
    for query in Query:
        if query[0] == 4:
            a, b = query[1], query[2]
            if t == 0:
                print(N*(G[a]-1) + (R[b]-1))
            else:
                print(N*(G[b]-1) + (R[a]-1))
            continue
        if query[0] == 3:
            t ^= 1
            # print("t")
            continue
        if (t == 0 and query[0] == 1) or (t == 1 and query[0] == 2):
            a, b = query[1], query[2]
            if a == b:
                continue
            G[a], G[b] = G[b], G[a]
        else:
            a, b = query[1], query[2]
            # print(G,R)
            # print(a,b)
            if a == b:
                continue
            R[a], R[b] = R[b], R[a]
        # print(G, R)

if __name__ == '__main__':
    main()
