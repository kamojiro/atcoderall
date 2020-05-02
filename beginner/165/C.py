#import sys
#input = sys.stdin.readline
from itertools import combinations
def main():
    N, M, Q = map( int, input().split())
    ABCD = [ tuple( map( int, input().split())) for _ in range(Q)]
    ans = 0
    for C in combinations( range(N+M-1), M-1):
        A = []
        index = 0
        now = 1
        for i in range(N+M-1):
            if index < M-1:
                if C[index] == i:
                    now += 1
                    index += 1
                    continue
            A.append(now)

        lans = 0
        for a, b, c, d in ABCD:
            if A[b-1] - A[a-1] == c:
                lans += d
        if ans < lans:
            ans = lans
    print(ans)
    
if __name__ == '__main__':
    main()







