from collections import defaultdict
N, M = map( int, input().split())
S = list( input())
E = [ list( map( int, input().split())) for _ in range(M)]
V = [ 1 for _ in range(N)]
Edges = [set() for _ in range(N)]
A = [0]*N
B = [0]*N
d = defaultdict(int)
for i in range(M):
    a, b = E[i]
    a, b = a-1, b-1
    a, b = min(a,b), max(a,b)
    Edges[a].add(b) #隣接する頂点をメモする
    Edges[b].add(a)
    if d[(a,b)] == 1:#(a,b)という辺を一度入力しれいれば、無視して次のループに進む。
        continue
    else:#一度目の入力をしたことをメモする。
        d[(a,b)] += 1
    if a == b:#ループ(同じ頂点を結ぶ辺)だと、このあとの方法だと、ダブルカウントしてしまうので、別扱い。
        if S[a] == 'A':
            A[a] += 1
        else:
            B[a] += 1
        continue
    if S[a] == 'A':
        A[b] += 1
    else:
        B[b] += 1
    if S[b] == 'B':
        B[a] += 1
    else:
        A[a] += 1
T = set()

for i in range(N):#'A'と’B'のうち、高々1種類しか隣接していない頂点をTに追加する。
    if A[i] == 0 or B[i] == 0:
        T.add(i)

while T:#'A'と’B'のうち、高々1種類しか隣接していない頂点がなくなるまでループを回す。
    n = T.pop()#一つ取り出す。
    V[n] = 0#'A'と’B'のうち、高々1種類しか隣接していない頂点なので、取り除く。
    for m in Edges[n]:#頂点nが消えると、それに隣接する頂点mに隣接する'A'及び'B'の個数が1だけ減少する。
        if V[m] == 1:
            if S[n] == 'A':
                A[m] -= 1
                if A[m] == 0:#隣接する頂点mに隣接する'A'及び'B'の個数が0になると、次に消える頂点になる。
                    T.add(m)
            else:
                B[m] -= 1
                if B[m] == 0:#隣接する頂点mに隣接する'A'及び'B'の個数が0になると、次に消える頂点になる。
                    T.add(m)
                
if sum(V) == 0:
    print('No')
else:
    print('Yes')
    

