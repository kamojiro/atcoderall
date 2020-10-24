#import sys
#input = sys.stdin.readline

def permute(X, Y):
    # X is permuted by Y
    ret = [0]*len(X)
    for i, x in enumerate(X):
        ret[i] = Y[x]
    return ret
        
def main():
    N, M, D = map(int,input().split())
    A = list(map(int,input().split()))
    permutation = [i for i in range(N+1)]
    # print(permutation)
    for a in A:
        permutation[a], permutation[a+1] = permutation[a+1], permutation[a]
    now = [i for i in range(N+1)]
    while D > 0:
        if D%2 == 1:
            now = permute(now, permutation)
        D //= 2
        permutation = permute(permutation, permutation)
    ANS = [0]*(N+1)
    for i, x in enumerate(now):
        ANS[x] = i
    print("\n".join(map(str, ANS[1:])))
if __name__ == '__main__':
    main()
