#import sys
#input = sys.stdin.readline
from collections import deque, Counter
def main():
    N = int( input())
    A = [ input() for _ in range(N)]
    CA = [ Counter(a) for a in A]
    ANS = []
    for i in range(N//2):
        for c in CA[i]:
            if CA[N-1-i][c] > 0:
                ANS.append(c)
                break
        else:
            print(-1)
            return
    if N%2 == 1:
        print( "".join(ANS) + A[N//2][0] + "".join(ANS[::-1]))
    else:
        print( "".join(ANS) + "".join(ANS[::-1]))
if __name__ == '__main__':
    main()
