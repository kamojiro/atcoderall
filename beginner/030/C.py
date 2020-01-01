#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    X, Y = map( int, input().split())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    now = 0
    airport = 0
    i = 0
    j = 0
    ans = 0
    while True:
        if airport == 0:
            while now > A[i]:
                i += 1
                if i >= N:
                    print(ans)
                    return
            airport = 1
            now = A[i] + X
        else:
            while now > B[j]:
                j += 1
                if j >= M:
                    print(ans)
                    return
            airport = 0
            ans += 1
            now = B[j] + Y

if __name__ == '__main__':
    main()
