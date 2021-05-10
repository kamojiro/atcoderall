#import sys
#input = sys.stdin.readline
def main():
    K, N, M = map(int, input().split())
        
    A = list(map(int,input().split()))

    l = 0
    r = N*M
    for _ in range(500):
        m = (l+r)//2
        z = 0
        f = M
        check = True
        for a in A:
            if a*M <= m:
                z += (a*M+m)//N
                continue
            if (a*M-m+N-1)//N > f:
                check = False
                break
            f -= abs(a*M-m+N-1)//N
            z += (a*M+m)//N
        if f > z:
            check = False
        if check:
            r = m
        else:
            l = m
    # print(l, r)
    ANS = [0]*K
    f = M
    for i, a in enumerate(A):
        ANS[i] += (a*M-r+N-1)//N
        f -= (a*M-r+N-1)//N
    # print(ANS)
    for i, a in enumerate(A):
        if f == 0:
            break
        # print((a*M+r)//N)
        ANS[i] += min((a*M+r)//N - (a*M-r+N-1)//N, f)
        f -=  min((a*M+r)//N - (a*M-r+N-1)//N, f)
    ANS[0] += M-sum(ANS)
    print(" ".join(map(str,map(int, ANS))))
        
            
if __name__ == '__main__':
    main()
