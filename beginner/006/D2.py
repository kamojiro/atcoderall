import sys
input = sys.stdin.readline
from bisect import bisect_left
def main():
    N = int( input())
    C = [ int( input()) for _ in range(N)]
    ANS = [N+1]*(N+1)
    ANS[0] = -1
    for c in C:
        l = bisect_left(ANS, c)
        ANS[l] = c
    ans = N
    for i in range(N+1):
        if ANS[i] == N+1:
            ans = i-1
            break
    print(N-ans)
if __name__ == '__main__':
    main()
