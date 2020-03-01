import sys
input = sys.stdin.readline
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
    N = int( input())
    S = list( input())
    Q = int( input())
    Query = [ tuple( input().split()) for _ in range(Q)]
    for i in range(40):
        if N < pow(2,i):
            n = pow(2,i)
            break
    A = [SegmentTree(n, 0, lambda a,b : a+b) for _ in range(26)]
    a = ord('a')
    for i in range(N):
        A[ord(S[i]) - a].update(i, 1)
    ANS = []
    for t, i, c in Query:
        if t == '1':
            i = int(i)
            A[ord(S[i-1])-a].update(i-1, 0)
            A[ord(c)-a].update(i-1,1)
            S[i-1] = c
        else:
            i, c = int(i), int(c)
            ans = 0
            for j in range(26):
                if A[j].query(i-1, c) > 0:
                    ans += 1
            ANS.append(ans)
    print('\n'.join( map(str, ANS)))

if __name__ == '__main__':
    main()
