#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = [(A[i], i) for i in range(N)]
    B.sort( reverse=True)
    ANS = [-1]*(N+1)
    m = 0
    M = N-1
    ans = 0
    for b, i in B:
        if i-m <M-i:
            ans += b*(M-i)
            M -= 1
        elif i-m > M-i:
            ans += b*(i-m)
            m += 1
        else:
            if A[m] <= A[M]:
                ans += b*(i-m)
                m += 1
            else:
                ans += b*(M-i)
                M -= 1
                #        print(b,i,ans)
    print(ans)
            
if __name__ == '__main__':
    main()
