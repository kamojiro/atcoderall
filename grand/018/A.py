#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    A.sort()
    if A[-1] < K:
        print('IMPOSSIBLE')
        return
    g = A[0]
    if A[0] == K:
        print('POSSIBLE')
        return
    for i in range(N-1):
        if A[i+1] == K:
            print('POSSIBLE')
            return
        g = gcd(g, A[i+1]-A[i])
    if K < g:
        print('IMPOSSIBLE')
        return
    if K%g == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
if __name__ == '__main__':
    main()
