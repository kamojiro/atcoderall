#import sys
#input = sys.stdin.readline
def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
#    bx, by = sorted([find(A,x), find(A,y)]) # bx, by = find(A,x), find(A,y)だと無限ループ。
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

def main():
    N = int( input())
    XY = []
    for i in range(N):
        x, y = map( int, input().split())
        XY.append( (x,y,i))
    
    XY.sort(key=lambda x:x[0])
    A = [ i for i in range(N)]
    my = N+1
    myi = N+1
    for x,y,i in XY:
        if y < my:
            my = y
            myi = i
            continue
        union(A, i , myi)
    My = 0
    Myi = N+1
    for x, y, i in XY[::-1]:
        if y > My:
            My = y
            Myi = i
            continue
        union(A, i, Myi)

    XY.sort(key=lambda x:x[1])
    mx = N+1
    mxi = N+1
    for x,y,i in XY:
        if x < mx:
            mx = x
            mxi = i
            continue
        union(A, i , mxi)
    Mx = 0
    Mxi = N+1
    for x, y, i in XY[::-1]:
        if x > Mx:
            Mx = x
            Mxi = i
            continue
        union(A, i, Mxi)
 
    T = [0]*N
    for i in range(N):
        T[find(A,i)] += 1
   
    
    ANS = [0]*N
    for i in range(N):
        ANS[i] = T[ find(A,i)]
    print("\n".join( map( str, ANS)))
                 
if __name__ == '__main__':
    main()
