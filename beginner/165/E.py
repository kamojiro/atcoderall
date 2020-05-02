#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    ANS = []
    if N%2 == 1:
        n = N//2
        for i in range(M):
            ANS.append([n-i, n+1+i])
    else:
        n = N//2
        t = 0
        for i in range(M):
            if i%2 == 0:
                ANS.append([n-i//2, n+1+i//2])
            else:
                ANS.append([(i+1)//2, N-(i+1)//2])

    print( "\n".join( [" ".join( map( str,ans)) for ans in ANS]))
if __name__ == '__main__':
    main()
