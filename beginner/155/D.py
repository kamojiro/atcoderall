def minus_case(Ap, Am, plus, minus, K):
    l = -10**18-1
    r = -1
    while r-l > 1:
        m = (l+r)//2
        underm = 0
        j = minus-1
        now = Am[j]
        for a in Ap[::-1]:
            while now*a > m:
                j -= 1
                if j == -1:
                    break
                now = Am[j]
            if j == -1:
                break
            else:
                underm += j+1
        if underm < K:
            l = m
        else:
            r = m
    return r

def same_case(A, N, m):
    if N <= 1:
        return 0
    j = N-1
    ret = 0
    now = A[j]
    for a in A:
        while a*now > m:
            j -= 1
            if j == -1:
                break
            now = A[j]
        if j == -1:
            break
        else:
            if a <= A[j]:
                ret += j
            else:
                ret += j+1
    return ret//2

def plus_case(Ap, Am, plus, minus, K):
    # Am = [abs(a) for a in Am]
    # Am.sort()
    l = 0
    r = 10**18
    while r-l > 1:
        m = (l+r)//2
        underm = same_case(Ap,plus,m) + same_case(Am,minus,m)
        if underm < K:
            l = m
        else:
            r = m
    return r

def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    Ap = []
    Am = []
    zero = 0
    plus = 0
    minus = 0
    for a in A:
        if a == 0:
            zero += 1
        elif a > 0:
            plus += 1
            Ap.append(a)
        else:
            minus += 1
            Am.append(a)
    if K <= plus*minus:
        Ap.sort()
        Am.sort()
        ans = minus_case(Ap, Am, plus, minus,K)
    elif K <= zero*(plus+minus)+zero*(zero-1)//2 + plus*minus:
        ans = 0
    else:
        Ap.sort()
        Am = sorted([-a for a in Am])
        ans = plus_case(Ap, Am, plus, minus,K-(zero*(plus+minus)+zero*(zero-1)//2 + plus*minus))
    print(ans)
    
if __name__ == '__main__':
    main()
