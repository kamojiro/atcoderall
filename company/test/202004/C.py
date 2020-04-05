#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    a,b,c = map( int, input().split())
    N = a+b+c
    ans = 0
    for P in permutations( range(N)):
        check = True
        for i in range(N-1):
            if i == a-1:
                continue
            if i == a+b-1:
                continue
            if P[i] >= P[i+1]:
                check = False
                break
        for j in range(b):
            if P[j] >= P[a+j]:
                # print(P[j], P[a+j])
                check = False
                break
        for j in range(c):
            # print(P[j], P[a+b+j])
            if P[a+j] >= P[a+b+j]:
                check = False
                break
        # print(P, check)
        if not check:
            continue
        # print(P)
        ans += 1
    print(ans)
if __name__ == '__main__':
    main()
