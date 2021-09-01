#import sys
#input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int,input().split()))
    Z = []
    for i in range(N-1):
        for j in range(i+1, N):
            Z.append(A[i]*A[j])
    Z.sort()
    print(Z)
    
    print(Z[K-1])
if __name__ == '__main__':
    main()
