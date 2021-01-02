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
    ans = 0
    V = [0]*W
    t = W
    Yoko = [True]*(W+1)
    if G[0]:
        t = G[0][0]-1
    for i in range(t):
        add(V,i+1,1, W)
    for i in range(t,W):
        Yoko[i+1] = False
    ans += t
    left = True
    for g in G[1:]:
        # print(ans)
        if left:
            if g:
                ans += g[0]-1
                if g[0] == 1:
                    left = False
            else:
                ans += W
                continue
        
        for y in g:
            if Yoko[y]:
                Yoko[y] = False
                add(V,y,-1,W)
        if g:
            if left:
                ans += sums(V,W) - sums(V,g[0])
            else:
                ans += sums(V,W)
        else:
            if left:
                ans += W # not 
            else:
                ans += sums(V,W)
    print(ans)
    
            
            
            
if __name__ == '__main__':
    main()
