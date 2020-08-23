#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    H, W, M = map( int, input().split())
    HW = [ tuple( map( int, input().split())) for _ in range(M)]
    R = [0]*H
    C = [0]*W
    d = defaultdict( lambda : False)
    for h, w in HW:
        R[h-1] += 1
        C[w-1] += 1
        d[(h-1,w-1)] = True
    MR = max(R)
    MC = max(C)
    ans = MR+MC-1
    NR = []
    NC = []
    for index, r in enumerate(R):
        if r == MR:
            NR.append(index)
    for index, c in enumerate(C):
        if c == MC:
            NC.append(index)
    # print(NR)
    # print(NC)
    # print(ans,d)
    for r in NR:
        for c in NC:
            if not d[(r,c)]:
                # print(r,c)
                print(ans+1)
                return
    print(ans)
    # 自身を除く
    
if __name__ == '__main__':
    main()
