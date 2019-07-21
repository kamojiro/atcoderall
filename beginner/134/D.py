#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = [0] + list( map( int, input().split()))
    ANS = [0]*(N+1)
    for i in range(N,0,-1):
        t = sum([ANS[i*(j+1)] for j in range(N//i)] )%2
        if t == A[i]:
            continue
        ANS[i] = 1
    print( sum(ANS))
    print( " ".join( map( str, [ i for i in range(N+1) if ANS[i] == 1])))
if __name__ == '__main__':
    main()
