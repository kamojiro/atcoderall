#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    ANS = [1]*N
    for _ in range(K):
        d = int( input())
        A = list( map( lambda x: int(x)-1, input().split()))
        for a in A:
            ANS[a] = 0
    print( sum(ANS))
if __name__ == '__main__':
    main()
