#import sys
#input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    A.sort()
    aaa = [0]*(10**5+1)
    d = defaultdict(int)
    appA = [0]*(N+1)
    for i in range(N,0,-1):
        appA[i-1] = A[i-1] + appA[i]
#    print(appA)
    for a in A:
        aaa[a] += 1
        d[a] += 1
    for i in range(10**5, 0, -1):
        aaa[i-1] += aaa[i]
    l = 0
    r = 2*10**5+1
    while r - l > 1:
        m = (l+r)//2
        check = True
        cnt = 0
        for k, v in d.items():
            if m - k > 10**5:
                continue
            cnt += v*aaa[max(m-k, 0)]
#        print(m, cnt, l ,r)
        if cnt >= M:
            l = m
        else:
            r = m
    ans = 0
    m = 0
    for k, v in d.items():
        if l - k > 10**5:
            continue
        if k + A[-1] < l:
            continue
        ans += k*v*(N - bisect_left(A, l-k))+appA[ bisect_left(A, l-k)]*v

        m += v*(N - bisect_left(A, l-k))
    if m > M:
        ans -= l*(m-M)
    print(ans)
if __name__ == '__main__':
    main()
