#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    d = defaultdict( int)
    B = [ i for i in range(N)]
    for i in range(N-1,-1,-1):
        a = A[i]
        if d[a] > 0:
            B[i] = d[a]
        d[a] = i
    R = []
    R.append(B)
    for i in range(59):
        S = [R[i][R[i][j]] for j in range(N)]
        R.append(S)
    print(R)
            
    
        
    
if __name__ == '__main__':
    main()
