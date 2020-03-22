#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    A = list( map( int, input().split()))
    C = Counter(A)
    ans = 0
    ANS = []
    for t in C:
        ans += C[t]*(C[t]-1)//2
    for a in A:
        if C[a] == 1:
            ANS.append(ans)
            continue
        ANS.append( ans - C[a]*(C[a]-1)//2 + (C[a]-1)*(C[a]-2)//2)
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
