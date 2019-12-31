#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    Q = list( map( int, input().split()))
    P = [0]*N
    for i in range(N):
        P[Q[i]-1] = i+1
    A = [1]
    B = [1]
    for i in range(N-1):
        if P[i] < P[i+1]:
            A.append(A[-1] + P[i+1] - P[i] + 1)
        else:
            A.append(A[-1] + 1)
    for i in range(N-2,-1,-1):
        if P[i] > P[i+1]:
            B.append(B[-1] + P[i] - P[i+1] + 1)
        else:
            B.append(B[-1]+1)
    print(" ".join( map(str, A)))
    print(" ".join( map(str, B[::-1])))
if __name__ == '__main__':
    main()
