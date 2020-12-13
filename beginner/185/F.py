#import sys
#input = sys.stdin.readline
def add(A,a,w,N):#リストに値を追加する関数
    x = a
    while x <= N:
        A[x-1] ^= w
        x += x&(-x)

def sums(A,a):#k番目までの和
    x = a
    S = 0
    while x != 0:
        S ^= A[x-1]
        x -= x&(-x)
    return S

def main():
    N, Q = map( int, input().split())
    A = list( map( int, input().split()))
    TXY = [ tuple( map( int, input().split())) for _ in range(Q)]
    V = [0]*N
    for i, a in enumerate(A):
        add(V,i+1,a,N)
    # for i in range(1,N+1):
        # print(sums(V,i))
    ANS = []
    for t, x, y in TXY:
        if t == 1:
            add(V,x,y,N)
        else:
            # print(sums(V,x-1),sums(V,y))
            ANS.append(sums(V,y)^sums(V,x-1))
    print("\n".join(map(str,ANS)))
if __name__ == '__main__':
    main()
