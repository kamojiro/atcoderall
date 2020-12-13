#import sys
#input = sys.stdin.readline

#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    P = list( map( int, input().split()))
    ANS = []
    Z = [0]*(N+1)
    for i, p in enumerate(P):
        Z[p] = i
    permuted = [False]*N
    for n in range(1,N+1):
        if Z[n] == n-1:
            continue
        K = Z[n]
        for i in range(K-1,n-2,-1):
            if permuted[i]:
                print(-1)
                return
            ANS.append(i+1)
            Z[P[i+1]] = i
            Z[P[i]] = i+1
            P[i], P[i+1] = P[i+1], P[i]
            permuted[i] = True

    s = 0
    for p in permuted:
        if p:
            s += 1
            
    if s < N-1:
        print(-1)
        return
    print("\n".join(map(str, ANS)))
    
if __name__ == '__main__':
    main()
