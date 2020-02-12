#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    S = [ int(s) for s in input()][::-1]
    ANS = []
    t = 0
    while t < N:
        for i in range( min(M, N-t),0,-1):
            if S[t+i] == 0:
                ANS.append(i)
                t += i
                break
        else:
            print(-1)
            return
    if sum(ANS) == N:
        print( " ".join( map( str,ANS[::-1])))
    else:
        print(-1)
                

if __name__ == '__main__':
    main()
