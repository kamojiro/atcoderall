import sys
input = sys.stdin.readline
Q = 10**9+7
def main():
    H, W = map( int, input().split())
    A = []
    for _ in range(H):
        A.extend(list( map( int, input().split())))
    #A = [ list( map( int, input().split())) for _ in range(H)]
    L = []
    for i in range(H*W):
        L.append((A[i],i))
    L.sort()
    #B = [[1]*W for _ in range(H)]
    B = [1]*(H*W)
    #     m = L[0][0]
    T = H*W
    for a, i in L:
        if i - W >= 0:
            if A[i-W] < a:
                B[i] += B[i-W]
        if i + W <  T:
            if A[i+W] < a:
                B[i] += B[i+W]
        if i%W > 0:
            if A[i-1] < a:
                B[i] += B[i-1]
        if i%W+1 < W:
            if A[i+1] < a:
                B[i] += B[i+1]
        B[i] %= Q
    ans = 0
    # for b in B:
    #     ans += b
    #     ans %= Q
    print( sum(B)%Q)
    #print(ans)
        
if __name__ == '__main__':
    main()
