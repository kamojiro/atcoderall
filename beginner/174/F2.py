class SegmentTree():
    # SegmentTree(n, 0, lambda a,b : a+b)
    # 0-indexed
    def __init__(self,size,unit,f):
        self.size=size
        self.data=[unit for _ in range(2*size)]
        self.unit=unit
        self.f=f
    def update(self,i,x):
        c=self.data
        f=self.f
        i+=self.size
        c[i]=x
        while i>1:
            i//=2
            c[i]=f(c[i*2],c[i*2+1])
    def add(self,i,x):
        c=self.data
        f=self.f
        i+=self.size
        c[i]=f(c[i],x)
        while i>1:
            i//=2
            c[i]=f(c[i*2],c[i*2+1])
    def query(self,l,r):
        #[l,r)
        # print(l,r,self.data)
        c=self.data
        f=self.f
        x=self.unit
        y=self.unit
        l+=self.size
        r+=self.size
        while l<r:
            if l%2:
                x=f(x,c[l])
                l+=1
            if r%2:
                r-=1
                y=f(c[r],y)
            l//=2
            r//=2
        return f(x,y)

def main():
    N, Q = map( int, input().split())
    C = list( map( int, input().split()))
    LR = [ tuple( map( int, input().split())) for _ in range(Q)]
    LRI = [(x[1], x[0], i) for i, x in enumerate(LR)]
    # for i, x in enumerate(LR):
    #     LRI.append((x[1], x[0], i))
    LRI.sort()
    lastAppend = [-1]*(N+1)
    for i in range(40):
        if N < pow(2,i):
            n = pow(2,i)
            break
    Seg = SegmentTree(n, 0, lambda a,b : a+b)
    ANS = [0]*Q
    now = 1
    for r, l, i in LRI:
        while now <= r:
            c = C[now-1]
            if lastAppend[c] == -1:
                Seg.update(now-1,1)
            else:
                Seg.update(now-1,1)
                Seg.update(lastAppend[c],-1)
            lastAppend[c] = now-1          
            now += 1
        ANS[i] = Seg.query(l-1,r+1)
    print( "\n".join( map( str, ANS)))
    
    

if __name__ == '__main__':
    main()
