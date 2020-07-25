#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int,input().split())
    A = list( map( int, input().split()))
    ANS = []
    for i in range(K,N):
        if A[i-K] < A[i]:
            ANS.append("Yes")
        else:
            ANS.append("No")
    print("\n".join(ANS))
if __name__ == '__main__':
    main()
