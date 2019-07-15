#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    N = int( input())
    A = list( map( int, input().split()))
    S = sum(A)//2
    ANS = [0]*N
    Odd = [0]*((N+1)//2)
    Even = [0]*(N//2)
    for i in range((N+1)//2):
        Odd[i] = A[i*2]
    for j in range(N//2):
        Even[j] = A[j*2+1]
    accOdd = [0] + list( accumulate(Odd))
    accEven = [0] + list( accumulate(Even))
    ANS = [0]*N

    for i in range((N+1)//2):
        ANS[i*2] = (S - (accEven[-1] - accEven[i] + accOdd[i]))*2
    for i in range(N//2):
        ANS[i*2+1] = (S - (accOdd[-1]-accOdd[i+1] + accEven[i]))*2
    print( " ".join( map( str, ANS)))
if __name__ == '__main__':
    main()
