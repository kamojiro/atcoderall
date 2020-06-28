import sys
input = sys.stdin.readline
# from collections import defaultdict
def main():
    N = int( input())
    A = list( map( int, input().split()))
    Q = int( input())
    BC = [ tuple( map( int, input().split())) for _ in range(Q)]
    L = [0]*(10**5+1)
    ans = sum(A)
    for a in A:
        L[a] += 1
    ANS = []
    for b, c in BC:
        ans = ans + L[b]*c - L[b]*b
        L[c] += L[b]
        L[b] = 0
        ANS.append(ans)

    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()



