#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( range(1,N+1))
    for i in range(N):
        print(A[i:]+A[:i])
if __name__ == '__main__':
    main()
