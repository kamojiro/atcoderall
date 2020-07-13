#import sys
#input = sys.stdin.readline
from itertools import product
def check(C,p,q,H,W):
    ret = 0
    for i in range(H):
        if p[i] == 1:
            continue
        for j in range(W):
            if q[j] == 1:
                continue
            if C[i][j] == "#":
                ret += 1
    return ret

def main():
    H, W, K = map( int, input().split())
    C = [ list( input()) for _ in range(H)]
    ans = 0
    for p in product(range(2), repeat=H):
        for q in product(range(2), repeat=W):
            if check(C,p,q,H,W) == K:
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()








