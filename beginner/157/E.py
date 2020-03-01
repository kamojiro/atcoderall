import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, unit): #example (12, min, 2**31-1)
        for k in range(40):
            if 2**k > n:
                break
        self.powers = pow(2,k)
        self.segTree = [unit]*(2*self.powers)
        self.unit = unit
    
    def update(self, i, x):#i番目(0-indexed)にx代入, segTree = [0,*,*,...], 1-indexed, N < k
        i += self.powers
        self.segTree[i] = x
        while i > 1:
            i //= 2
            self.segTree[i] = self.segTree[i*2] + self.segTree[i*2+1]

    def getCal(self, i, j, k=1, l=0, r=-1): #get self.cal of [i,j)!!!!!
        if r < 0: #initization, we want to r = self.powers as an initial value.
            r = self.powers
        if j <= l or r <= i:
            return self.unit
        if i <= l and r <= j:
            return self.segTree[k]
        return self.getCal(i ,j, k*2, l, (l+r+1)//2) + self.getCal(i ,j, k*2+1, (l+r+1)//2, r)


def main():
    N = int( input())
    S = list( input())
    Q = int( input())
    Query = [ tuple( input().split()) for _ in range(Q)]
    A = [SegmentTree(N, 0) for _ in range(26)]
    a = ord('a')
    for i in range(N):
        A[ord(S[i]) - a].update(i, 1)
    ANS = []
    for t, i, c in Query:
        if t == '1':
            i = int(i)
            A[ord(S[i-1])-a].update(i-1, 0)
            A[ord(c)-a].update(i-1,1)
        else:
            i, c = int(i), int(c)
            ans = 0
            for j in range(26):
                if A[j].getCal(i-1, c) > 0:
                    ans += 1
            ANS.append(ans)
    print('\n'.join( map(str, ANS)))
if __name__ == '__main__':
    main()
