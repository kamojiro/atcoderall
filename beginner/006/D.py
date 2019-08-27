import sys
input = sys.stdin.readline
def main():
    N = int( input())
    C = [0] + [ int( input()) for _ in range(N)]
    ANS = [0]*(N+1)
    for i in range(N):
        c = C[i+1]
        now = 0
        for j in range(i+1):
            if C[j] < c and ANS[j] > now:
                now = j
        ANS[i+1] = ANS[now] + 1
    print( N - max(ANS))
if __name__ == '__main__':
    main()
