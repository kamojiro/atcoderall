#import sys
#input = sys.stdin.readline
from itertools import product
from bisect import bisect_left
def main():
    N, T = map(int,input().split())
    A = list(map(int,input().split()))
    # if N == 1:
    #     if A[0] <= T:
    #         print(A[0])
    #     else:
    #         print(0)
    #     return
    KA = A[:N//2]
    KB = A[N//2:]
    SA = set([0])
    SB = set([0])
    for p in product(range(2),repeat=N//2):
        t = 0
        for i,c in enumerate(p):
            if c == 1:
                t += KA[i]
        if t <= T:
            SA.add(t)
    
    for p in product(range(2),repeat=N-N//2):
        t = 0
        for i,c in enumerate(p):
            if c == 1:
                t += KB[i]
        if t <= T:
            SB.add(t)
    LA = sorted(list(SA))
    LB = sorted(list(SB))
    MB = LB[-1]
    ans = 0
    for a in LA:
        t = T-a
        if t == 0:
            print(T)
            return
        if MB <= t:
            z = MB+a
        else:
            index = bisect_left(LB, t)
            if t == LB[index]:
                print(T)
                return
            z = a+LB[index-1]
        if z > ans:
            ans = z
    # print(LA, LB)
    print(ans)


    
    
if __name__ == '__main__':
    main()
