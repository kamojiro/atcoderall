class SegTreeMin:
    def __init__(self, n):
        self.n = n
        # nより大きい2の冪数
        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [float('inf')] * (n2 << 1)
 
    def update(self, i, x):
        i += self.n2
        self.tree[i] = x
        while i > 1:
            self.tree[i >> 1] = x = min(x, self.tree[i ^ 1])
            i >>= 1
 
    def get_min(self, a, b):

        return self._get_min(a, b, 1, 0, self.n2)

    def _get_min(self, a, b, k, l, r):
        # 範囲外ならINF
        if r <= a or b <= l:
            return float('inf')
        # [a,b)が完全に[l,r)を包含するならtree[k]の値を採用
        if a <= l and r <= b:
            return self.tree[k]
        # 一部だけ範囲内なら2つに分けて再帰的に調査
        m = (l + r) // 2
        return min(
            self._get_min(a, b, k << 1, l, m),
            self._get_min(a, b, (k << 1) + 1, m, r)
        )

N, K = map( int, input().split())
A = list( map( int, input().split()))
A = A[::-1]
st = SegTreeMin(N)
for i in range(N):
    st.update(i,A[i])
now = 0
ans = 0
while now <= N:
    m = st.get_min(now, min(now + K, N))
    bef = now
    for i in range( min(now+K-1, N-1), now-1, -1):
        if A[i] == m:
            now = m+1
            break
    ans += m*(now - bef)
print(ans)
