#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    ANS = [ [0]*N for _ in range(N)]
    for i in range(11):
        if N <= pow(2,i):
            M = i
            break
    # for s in range(1, N, 2):
    #     for i in range(N-s):
    #         ANS[i][i+s] = 1
    for t in range(1,M+1):
        w = pow(2,t-1)
        for s in range(1,N+1, 2):
            if w*s >= N:
                break
            for i in range(N-s*w):
                if ANS[i][i+w*s] == 0:
                    ANS[i][i+w*s] = t
    for i in range(N-1):
        print( " ".join( map( str, ANS[i][i+1:])))
if __name__ == '__main__':
    main()






