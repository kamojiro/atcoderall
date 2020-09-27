#import sys
#input = sys.stdin.readline
class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res



def main():
    N, Q = map( int, input().split())
    Query = [0]*Q
    for i in range(Q):
        Query[i] = tuple( map( int, input().split()))
    X = SegmentTree(N, f=lambda x, y : min(x,y), default=N-1)
    Y = SegmentTree(N, f=lambda x, y : min(x,y), default=N-1)
    ans = (N-2)*(N-2)
    for q, x in Query:
        if x == 1:
            t = X.query(x-1,N)
            Y.update(t,x-1)
            ans -= (t-1)
        else:
            t = Y.query(x-1,N)
            X.update(t,x-1)
            ans -= (t-1)            
    
    # for q, x in Query:
    #     if x == 1:
    #         Z = X
    #         W = Y
    #     else:
    #         Z = Y
    #         W = X
    #     t = Z.query(x-1,N)
    #     print(t)
    #     W.update(t,x)
    #     ans -= t-2
    #     print(W.query(t,t+1 ))
    for i in range(N):
        print( X.query(i,i+1))
    for i in range(N):
        print( Y.query(i,i+1))

    print(ans)
        
        
if __name__ == '__main__':
    main()
