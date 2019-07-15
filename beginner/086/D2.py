import sys
from itertools import accumulate
input = sys.stdin.readline
def main():
    N, K = map( int ,input().split())
    TK = K*2
    B = [[0]*(K*2) for _ in range(TK)]
    for _ in range(N):
        x, y, c = input().split()
        x, y = int(x), int(y)
        if c == "B":
            B[x%TK][y%TK] += 1
        else:
            B[x%TK][(y+K)%TK] += 1
    C = [[0]*(TK+1)] + [[0] + list( accumulate(B[i])) for i in range(TK)]
    for i in range(TK):
        for j in range(TK+1):
            C[i+1][j] += C[i][j]
    def get(i1, j1, i2, j2):
        return C[i2][j2] - C[i1][j2] - C[i2][j1] + C[i1][j1]
    ans = 0
    for i in range(K+1):
        for j in range(K+1):
            if ans < get(0,0,i,j) + get(i+K, 0, TK, j) + get(i, j, i+K, j+K) + get(0, j+K, i, TK) + get(K+i, K+j, TK, TK):
                ans = get(0,0,i,j) + get(i+K, 0, TK, j) + get(i, j, i+K, j+K) + get(0, j+K, i, TK) + get(K+i, K+j, TK, TK)
            if ans < get(i, 0, i+K, j) + get(0, j, i, j+K) + get(i+K, j, TK, j+K) + get(i, j+K, i+K, TK):
                ans = get(i, 0, i+K, j) + get(0, j, i, j+K) + get(i+K, j, TK, j+K) + get(i, j+K, i+K, TK)
    print(ans)
if __name__ == '__main__':
    main()
