#import sys
#input = sys.stdin.readline
def main():
    K, T = map( int, input().split())
    A = list( map( int, input().split()))
    A.sort(reverse=True)
    if A[0] <= (K+1)//2:
        print(0)
    else:
        print((A[0] - (K+1)//2)*2 - (K+1)%2)
if __name__ == '__main__':
    main()
