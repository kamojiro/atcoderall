def f(a, m):
    return a**2%m

def main():
    N, X, M = map( int, input().split())
    A = [X]
    T = [False]*M
    T[X] = True
    now = X
    while True:
        now = f(now, M)
        if T[now]:
            break
        T[now] = True
        A.append(now)
    R = len(A)
    for i in range(R-1,-1,-1):
        if now == A[i]:
            L = i
            break
    # L<= < Rでループ、R-L
    if N <= L:
        print( sum(A[:N]))
        return
    ans = sum(A[:L])
    loopsum = sum(A[L:])
    loopsize = R-L
    N -= L
    ans += N//loopsize*loopsum
    N -= N//loopsize*loopsize
    now = A[L]
    while N > 0:
        ans += now
        now = f(now,M)
        N -= 1
    print(ans)
if __name__ == '__main__':
    main()
