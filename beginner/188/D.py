#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    N, C = map(int,input().split())
    ABC = [ tuple(map(int,input().split())) for _ in range(N)]
    d = dict()
    Z = set()
    for a, b, _ in ABC:
        Z.add(a)
        Z.add(b+1)
    Z = list(Z)
    Z.sort()
    Z.append(Z[-1]+1)
    for i, z in enumerate(Z):
        d[z] = i
    M = len(Z)
    A = [0]*(M+1)
    for a, b, c in ABC:
        A[d[a]] += c
        A[d[b+1]] -= c
    # print(A)
    accA = list(accumulate(A))
    # print(accA, Z)
    ans = 0
    for i in range(M-1):
        if accA[i] <= C:
            ans += accA[i]*(Z[i+1]-Z[i])
            # print(accA[i]*(Z[i+1]-Z[i]))
        else:
            ans += C*(Z[i+1]-Z[i])
    print(ans)
    
if __name__ == '__main__':
    main()
