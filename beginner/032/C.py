import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, K = map( int, input().split())
    S = [ int( input()) for _ in range(N)]
    for s in S:
        if s == 0:
            print(N)
            return

    if K == 0:
        print(0)
        return
        
    d = deque()
    pro = 1
    length = 0
    ans = 0
    for s in S:
        pro *= s
        length += 1
        d.append(s)
        while (pro > K) and (length > 0):
            pro //= d.popleft()
            length -= 1
        if length > ans:
            ans = length
    print(ans)
            
        
if __name__ == '__main__':
    main()
