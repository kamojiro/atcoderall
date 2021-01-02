#import sys
#input = sys.stdin.readline
def add(A,a,w,N):#リストに値を追加する関数
    x = a
    while x <= N:
        A[x-1] += w
        x += x&(-x)

def sums(A,a):#k番目までの和
    x = a
    S = 0
    while x != 0:
        S += A[x-1]
        x -= x&(-x)
    return S

def main():
    H, W, M = map( int, input().split())
    G = [[] for _ in range(H)]
    XY = [ tuple( map( int, input().split())) for _ in range(M)]
    XY.sort()
    for x, y in XY:
        G[x-1].append(y)
    for i in range(H):
        G[i].append(W+1)
    Yoko = [True]*(W+2)
    Yoko[-1] = False
    ans = 0
    f = -1
    left = False

    V = [0]*(W+2)
    for i in range(W):
        add(V, i+1,1,W+1)
    # print(sums(V,4))
    for g in G:
        non_dup = 0
        c = 0
        if left:
            c = 0
        else:
            # print("s",g[0]-1)
            ans += g[0]-1
            c = 1
        if g[0] == 0:
            left = True
        for y in g[c:]:
            if Yoko[y]:
                non_dup += 1
        if c == 0:
            ans += sums(V, W+1)
            # print("d", sums(V, W))
        else:
            ans += sums(V, W+1) - sums(V,g[0]) - non_dup
            # print(sums(V, W+1), sums(V,g[0]), non_dup)
            # print("d",sums(V, W+1) - sums(V,g[0])-non_dup,g,g[0],  non_dup)
        for y in g:
            if Yoko[y]:
                add(V,y,-1,W+1)
                Yoko[y] = False
        # print(ans)
    print(ans)
            
            
if __name__ == '__main__':
    main()
