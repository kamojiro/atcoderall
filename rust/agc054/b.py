#import sys
#input = sys.stdin.readline
from itertools import permutations,product
def game(p, A):
    t = 0
    a = 0
    for i in range(len(A)):
        if t <= a:
            t += A[p[i]]
        else:
            a += A[p[i]]
    return t, a

def comb(A):
    s = sum(A)//2
    N = len(A)
    ret = 0
    for p in product(range(2), repeat=N):
        g = 0
        for i in range(N):
            if p[i] == 1:
                g += A[i]
        if g == s:
            ret += 1
    return ret

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for p in permutations(range(N)):
        t, a = game(p, A)
        if t == a:
            ans += 1
    print("comb", comb(A))
    print(ans)
if __name__ == '__main__':
    main()
