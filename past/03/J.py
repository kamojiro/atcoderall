#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    D = [10**10] + [0]*N
    ANS = []
    for a in A:
        l = 0
        r = N+1
        while r - l > 1:
            m = (l+r)//2
            if D[m] < a:
                r = m
            else:
                l = m
        if r == N+1:
            ANS.append(-1)
            continue
        ANS.append(r)
        D[r] = a
    print("\n".join( map(str, ANS)))
if __name__ == '__main__':
    main()
