import sys
input = sys.stdin.readline
def main():
    X, Y, A, B, C = map( int, input().split())
    P = list( map( int, input().split()))
    Q = list( map( int, input().split()))
    R = list( map( int, input().split()))
    P.sort( reverse = True)
    Q.sort( reverse = True)
    R.sort( reverse = True)
    ANS = P[:X] + Q[:Y]
    ANS.sort()
    for i in range( min(X+Y, C)):
        if ANS[i] < R[i]:
            ANS[i] = R[i]
        else:
            break
    print( sum(ANS))
    
if __name__ == '__main__':
    main()
