import sys
input = sys.stdin.readline
from collections import Counter

def add(N,A,a,w):#リストに値を追加する関数
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

def remove(N, A, k):
    l = 0
    r = N
    while r - l > 1:
        m = (l+r)//2
        # print(m, sums(A,m))
        if sums(A,m) > k-1:
            r = m
        else:
            l = m
    # print(l,r)
    add(N,A,l,-1)
    return l
    
def main():
    Q = int( input())
    TX = [ tuple( map( int, input().split())) for _ in range(Q)]
    N = 2*10**5
    A = [0]*(2*10**5+1)
    ANS = []
    for t, x in TX:
        if t == 1:
            add(N,A,x+1,1)
        else:
            ANS.append( remove(N,A,x))
    if ANS:
        print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
