def add(A,a,w):#リストに値を追加する関数
    x = a
    while x <= N:
        A[x-1] += w
        x += x&(-x)

def mini(A,a):#k番目までの和
    x = a
    S = 0
    while x != 0:
        S += A[x-1]
        x -= x&(-x)
    return S

A = [0]*N
for i in range(1,N+1):
    add(A,i,V[i-1])

N, K = map( int, input().split())
A = list( map( int, input().split()))
A = A[::-1]

ind = 0
cost = A[i]
ans = 0
now = 0
searched = 0
while :
    while searched <= now + K -1:
        if 
        searched += 1
