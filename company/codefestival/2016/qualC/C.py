#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    N = int( input())
    T = list( map( int, input().split()))
    A = list( map( int, input().split()))
    ANS = [0]*N
    now = 0
    AC = [False]*N
    for i in range(N):
        if now < T[i]:
            ANS[i] = T[i]
            AC[i] = True
        now = T[i]
    now = 0
    for i in range(N-1,-1,-1):
        if now < A[i]:
            if AC[i]:
                if A[i] != T[i]:
                    print(0)
                    return
            else:
                if A[i] > T[i]:
                    print(0)
                    return
                else:
                    ANS[i] = A[i]
        now = A[i]
    # for i in range(N):
    #     if ANS[i] == 0:
    #         ANS[i] = min(A[i],B[i])
    ans = 1
    for i in range(N):
        if ANS[i] == 0:
            ans *= min(A[i],T[i])
            ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
