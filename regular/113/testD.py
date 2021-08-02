#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, M, K = map(int,input().split())
    ANS = set()
    Ks = [0]*K
    for p in product(range(K),repeat=N*M):
        A = [[p[i*M+j] for j in range(M)] for i in range(N)]
        now = []
        for i in range(N):
            a = K
            for j in range(M):
                if a > A[i][j]:
                    a = A[i][j]
            now.append(a)
        # Ks[min(now)] += 1
        for j in range(M):
            a = 0
            for i in range(N):
                if A[i][j] > a:
                    a = A[i][j]
            now.append(a)
        ANS.add(tuple(now))
    for ans in ANS:
        Ks[min(ans[:N])] += 1
    print(Ks)
    # print(z//())
    print(len(ANS))
                    
if __name__ == '__main__':
    main()
