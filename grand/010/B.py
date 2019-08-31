#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    N = int( input())
    A = list( map( int, input().split()))
    C = [0]*(N*2+2)
    L = [0]*(N*2+2)
    cnt = 0
    if sum(A)%(N*(N+1)//2) != 0:
        print("NO")
        return
    t = sum(A)//(N*(N+1)//2)
    for i in range(N):
        if (A[i] - A[i-1] + (N-1)*t)%N != 0:
            print("NO")
            return
        k =  (A[i] - A[i-1] + (N-1)*t)//N
        C[i] += t-k
        C[i+N] -= t-k
        cnt += t-k
        L[i+N] -= (t-k)*N
    S = list( accumulate(C))
    if cnt > t:
        print("NO")
        return
    for i in range(N*2+1):
        S[i+1] += S[i] + L[i+1]

    for i in range(N):
        if A[i] != S[i] + S[i+N]:
            print("NO")
            return
    print("YES")
    
            
if __name__ == '__main__':
    main()
