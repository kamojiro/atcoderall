import sys
input = sys.stdin.readline
def main():
    N = int( input())
    A, B = [], []
    for _ in range(N):
        a, b = map( int, input().split())
        A.append(a)
        B.append(b)
    A.reverse()
    B.reverse()
    cnt = 0
    for i in range(N):
        if (A[i]+cnt)%B[i] == 0:
            continue
        cnt += B[i] - (A[i]+cnt)%B[i]
    print(cnt)
if __name__ == '__main__':
    main()
