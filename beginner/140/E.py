#import sys
#input = sys.stdin.readline
from bisect import bisect_left
def main():
    N = int( input())
    P = list( map( int, input().split()))
    ans = 0
    C = [-1]*(N+1)
    for i in range(N):
        C[P[i]] = i
    R = [C[N]]
    for i in range(N-1, 1, -1):
        n = N - i
        t = bisect_left(R, C[i])
        if t == 0:
            l = 0
        elif t == 1:
            l = C[t-1]+1
        else:
            l = C[t-1] - C[t-2]
        if t == n:
            r = N - C[i]
        else:
            r = C[t] - C[i]
        ans += l*r
        if t == 0:
            l = C[i] + 1
        else:
            l = C[t] - C[i]
        if t == n:
            r = 0
        elif t == n-1:
            r = 

        R.insert(t, C[i])
        
            
if __name__ == '__main__':
    main()
