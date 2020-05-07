#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N, P = map( int, input().split())
    A = Counter(list( map( lambda x: int(x)%2, input().split())))
    zero = A[0]
    one = A[1]
    ans = 1
    now = 1
    for i in range(1,one+1):
        now *= (one-i+1)
        now //= i
        if i%2 == 0:
            ans += now
    if P == 0:
        print( ans*pow(2,zero))
    else:
        print(pow(2,N) - ans*pow(2,zero))
        
if __name__ == '__main__':
    main()
