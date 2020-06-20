import sys
input = sys.stdin.readline
from collections import Counter, defaultdict
def main():
    N = int( input())
    A = list( map( int, input().split()))
    CA = Counter(A)
    d = defaultdict( lambda : False)
    T = [False]*(10**6+1)
    A.sort()
    Z = [False]*(10**6+1)
    ans = 0
    for a in A:
        if CA[a] == 1 and not T[a]:
            ans += 1
        if not Z[a]:
            Z[a] = True
            for i in range(1, 10**6+1):
                if i*a > 10**6:
                    break
                T[i*a] = True
    print(ans)
if __name__ == '__main__':
    main()
