class BIT:
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
        self.bisect_K = [1 << k for k in reversed(range(N.bit_length()))]
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
    def bisect(self, w):
        if w <= 0:
            return 0
        bit, N = self.tree, self.size
        i = 0
        for k in self.bisect_K:
            if i + k <= N and bit[i + k] < w:
                i += k
                w -= bit[i]
        return i + 1


import sys
input = sys.stdin.readline
def main():
    Q = int( input())
    TX = [ tuple( map( int, input().split())) for _ in range(Q)]
    binary_indexed_tree = BIT(200010)
    ANS = []
    for t, x in TX:
        if t == 1:
            binary_indexed_tree.add(x,1)
        else:
            p = binary_indexed_tree.bisect(x)
            # ANS.append(p)
            print(p)
            binary_indexed_tree.add(p, -1)
    # print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
