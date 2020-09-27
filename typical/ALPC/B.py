import sys
input = sys.stdin.readline
#N個の変数v_1, ..., v_n
#Q個のクエリ
#各クエリはv_aにwを加えるという操作
#answerは各クエリに対してv_1 + ... + v_aを求める
#クエリごとにどんどんv_1, ..., v_nは更新される
#x-1となっているのは、リストが0番目からになっているから。
#x&(-x)で2進数で表した場合の最も下位にある1の位置を取り出すことができる。
#例えば，10 = 1010なら10を返し、7 = 111なら1を返す。
def main():
    N, Q = map( int, input().split())
    A = list( map( int, input().split()))
    bit = [0]*N
    def add(bit,a,w):#リストに値を追加する関数
        x = a
        while x <= N:
            bit[x-1] += w
            x += x&(-x)

    def sums(bit,a):#k番目までの和
        x = a
        S = 0
        while x > 0:
            S += bit[x-1]
            x -= x&(-x)
        return S

    for i, a in enumerate(A):
        add(bit,i+1,a)
    Q = [ tuple( map( int, input().split())) for _ in range(Q)]
    ANS = []
    for q,p,x in Q:
        if q == 0:
            add(bit,p+1,x)
        else:
            ANS.append( sums(bit,x)-sums(bit,p))
    print( "\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
