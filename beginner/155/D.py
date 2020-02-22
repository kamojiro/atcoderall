# import sys
# input = sys.stdin.readline
from bisect import bisect_left, bisect_right
from collections import defaultdict
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    Ap = []
    Am = []
    zero = 0
    d = defaultdict( int)
    for a in A:
        d[a] += 1
        if a > 0:
            Ap.append(a)
        elif a < 0:
            Am.append(-a)
        else:
            zero += 1
    lp = len(Ap)
    lm = len(Am)
    l = 0
    r = 10**18
    while r - l > 2:
        m = (l+r)//2
        cnt = 0
        if m >= 0:
            cnt += zero*(N-1)
            cnt += lp*lm
            for a in Ap:
                t = bisect_right(Ap, m//a)
                if t == 0:
                    continue
                cnt += t
                if Ap[t-1] <= a:
                    cnt -= 1
            for a in Am:
                t = bisect_right(Am, m//a)
                if t == 0:
                    continue
                cnt += t
                if Am[t-1] <= a:
                    cnt -= 1
        else:
            for a in Ap:
                t = bisect_left(Am,(-m+a-1)//a)
                cnt += t
                if t == lm:
                    continue
                cnt += lm-t
        if cnt < K:
            l = m
        else:
            r = m
    ans = -10**18
    if zero > 0 and r >= 0:
        ans = 0
    if r > 0:
        if not Am:
            

            
        for a in Ap:
            if d[a] > 0:
                if a**2 <= r:
                    if ans < a**2:
                        ans = a**2
            t = bisect_right(Ap, r//a)
            if t == 0:
                continue
            if Ap[t-1] == a:
                continue
            if Ap[t-1]*a > ans:
                ans = Ap[t-1]*a
        for a in Am:
            if d[-a] > 0:
                if a**2 <= r:
                    if ans < a**2:
                        ans = a**2
            t = bisect_right(Am, r//a)
            if t == 0:
                continue
            if Am[t-1] == a:
                continue
            if Am[t-1]*a > ans:
                ans = Am[t-1]*a
    if r < 0:
        for a in Ap:
            t = bisect_left(Am,(-r+a-1)//a)
            if t == lm:
                continue
            if ans < -Am[t+1]*a:
                ans = -Am[t+1]*a

#    print(r)
    print(ans)

    
if __name__ == '__main__':
    main()
