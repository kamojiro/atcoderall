import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    S = list( map( int, input().split()))
    S.sort(reverse=True)
    for i in range(N):
        if S[0] <= S[i+1]:
            print('No')
            return
    check = N+1
    for i in range(N-1):
        now = pow(2,i)
        for j in range(now):
            for _ in range(N-i-1):
                if S[now+j] <= S[check]:
                    print('No')
                    return
                check += 1

    print('Yes')

if __name__ == '__main__':
    main()
