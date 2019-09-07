import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    A = [deque()] + [deque( map( int, input().split())) for _ in range(N)]
    Days = [0]*(N+1)
    NOW = [0]*(N+1)
    # for i in range(1, N+1):
    #     a = A[i].popleft()
    #     if NOW[a] == i:
    #         Days[a] = Days[i] = max(Days[a], Days[i])
    q = deque( [ i+1 for i in range(N)])
    while q:
        i = q.popleft()
        if not A[i]:
            continue
        a = A[i].popleft()
        if NOW[a] == i:
            Days[a] = Days[i] = max(Days[a], Days[i])+1
            q.append(i)
            q.append(a)
            NOW[a] = NOW[i] = 0
        else:
            NOW[i] = a
    for i in range(1,N+1):
        if A[i]:
            print(-1)
            return
    print( max(Days))
if __name__ == '__main__':
    main()
